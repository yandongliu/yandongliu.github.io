---
layout: post
title:  "Non-blocking programming with Tornado"
date:   2016-04-18 17:12:22 -0800
categories: python tornado
---
`Tornado` is an asynchronous networking library. It's also a Web framework so you can write a whole website with it.

With Synchorous/blocking programming everything works sequentially: one function does its work and returns. If there is an I/O piece in it then its execution blocks until it finishes. When there is ten of thousands of excutions of such blocking functions a lot of CPU cycles are wasted doing nothing.

On the other hand non-blocking functions can return early to give CPU away, and a callback is triggered when that blocking event finishes. In `Tornado` the result early returned is called `Future`, and its result will be populated when that I/O work finishes.


{% highlight python %}
def foo():
    future = SomeIOWork()
    future.add_done_callback(lambda f: future.set_result(f.result()))
    return future
{% endhighlight %}

All this work is managed by its `IOLoop` behind the scene. If you look at above code it looks like nothing but getting the result from a dependent future, wrapping it in a new future and passing it out. To simplify this diagram one can simply use `coroutine` which essentially does above work for you:

{% highlight python %}
@coroutine
def foo():
    result = yield SomeIOWork()
    raise Return(result)  # for Python 2.7
{% endhighlight %}

## Some notes on writing Tornado code:
* Everything has to be non-blocking. Wrapping blocking code with `@coroutine` doesn't help.
* Yield a list of futures whenever you can. It's a lot faster than yield one by one.
* By reading the code it looks like a `coroutine` wouldn't return until it finishes first `yield` and this happens recursively. Therefore if you have lots of heavy work through first yield I doubt if it will be a lot faster.

## Coroutine performance benchmarking
Let's write a small HTTP endpoint in 3 different ways:

* **Asynchronous**: coroutine everywhere so nothing is blocking
* **Synchronous**: no coroutine
* **Sync + Coroutine**: coroutine everywhere except the HTTP client is blocking (`request`)

*Asynchronous* version:

{% highlight python %}
@gen.coroutine
def urls_to_check():
    return [
        'http://google.com',
        'http://wikipedia.org',
        'http://amazon.com',
    ]


class StatusCheckHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def check_status(self, url):
        client = AsyncHTTPClient()
        try:
            response = yield client.fetch(url)
        except Exception as e:
            raise gen.Return(('error', str(e)))
        raise gen.Return(('http-status', response.code))

    @gen.coroutine
    def get(self):
        statuses = {}
        status_futures = {
            url: self.check_status(url) for url in urls_to_check()
        }
        statuses = yield status_futures
        self.write(json.dumps(statuses))

def get_app():
    return tornado.web.Application([
        (r'/', StatusCheckHandler),
    ], debug=True, autoreload=True)

if __name__ == '__main__':
    app = get_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
{% endhighlight %}

*Synchronous* version: replace `AsyncHTTPClient` with `requests`:
{% highlight python %}
...
def check_status(url):
    try:
        return ('http-status', requests.get(url).status_code)
    except Exception as e:
        return ('error', str(e))
...
{% endhighlight %}

*Coroutine* version: wrap synchronous calls in a coroutine
{% highlight python %}
...
@gen.coroutine
def check_status(url):
    try:
        raise gen.Return(('http-status', requests.get(url).status_code))
    except Exception as e:
        raise gen.Return(('error', str(e)))
...
{% endhighlight %}

And here's the result (response time in *ms*):

*100 connections with 20 concurrency: `ab -n 100 -c 20 http://localhost:8080/`*

|         | Median           | p90%  | p99% |
| ------------- |:-------------:| -----:| -----:|
| Async | 4013 | 4521 | 4945 |
| Sync | 8085 | 8390 | 8683 |
| Sync + Coroutine | 30422 | 31565 | 32665 |


*500 connections with 50 concurrency: `ab -n 500 -c 50 http://localhost:8080/`*

| | Median           | p90%  | p99% |
| ------------- |:-------------:| -----:| -----:|
| Async | 9131 | 9381 | 9894 |
| Sync | 21510 | 22215 | 22833 |
| Sync + Coroutine | 77701 | 79787 | 81497 |

<br/>
If you can leverage truly non-blocking code everywhere it seems to be a huge performance boost. But any blocking code will slow it down if you execute it somewhere in the main `IOLoop`. In that case you may need to have a `Runner` in a different thread so that it doesn't block your primary IOLoop.
