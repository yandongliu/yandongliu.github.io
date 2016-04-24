---
layout: post
title:  "Go concurrency programming"
date:   2016-04-23 16:12:22 -0800
categories: go concurrency
---
`Go` is said to have great concurrency capability so I wanted to explore it. Similar to my previous `Tornado` benchmarking test I wrote some Go code that looks semantically similar:

{% highlight go %}
package main

import (
    "fmt"
    "net/http"
    "time"
)

func checkStatus(url string, c chan int) {
    resp, err := http.Get(url)
    if err != nil {
        c <- 400
    } else {
        c <- resp.StatusCode
    }
}

var requestCnt int

func statusHandler(w http.ResponseWriter, r *http.Request) {
    requestCnt++
    fmt.Printf("%d: %s\n", requestCnt, r.RemoteAddr)
    var urls = []string{
        "http://google.com",
        "http://yahoo.com",
        "http://amazon.com",
    }
    var c = make(chan int, len(urls))
    for _, url := range urls {
        go checkStatus(url, c)
    }
    var count = 0
    for {
        select {
        case r := <-c:
            fmt.Fprintf(w, "%d", r)
            count++
            if count == len(urls) {
                return
            }
        case <-time.After(50 * time.Millisecond):
            fmt.Printf(".")
        }
    }

}

func main() {
    requestCnt = 0
    http.HandleFunc("/", statusHandler)
    http.ListenAndServe(":8080", nil)
}

{% endhighlight %}

I used `goroutine` to fetch URLs simultaneously and query their status non-blockingly with `select` statement. I also had to run `ulimit -n 1000` before running `ab` otherwise I got "too many open files" complaint. 

And here's the result (response time in *ms*):

|         | Median           | p90%  | p99% |
| ------------- |:-------------:| -----:| -----:|
| 100 requests + 20 concurrency | | | |
| 500 requests + 50 concurrency | |  | |
