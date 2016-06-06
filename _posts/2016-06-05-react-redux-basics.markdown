---
layout: post
title:  "React/Redux basics"
date:   2016-06-05 16:12:22 -0800
categories: react redux
---

# ES6 Prime
Some ES6 new features that I think are immediately useful:
 - variable declaraton: `const`, `let`
 - arrow function:
{% highlight javascript %}
    const getName = (item) => { return item.name } 
 - property shorthand:
{% endhighlight %}
    obj = {name, score} // === obj = {name:name, score:score}
{% highlight javascript %}
{% endhighlight %}
 - class:
{% highlight javascript %}
class Shape {
    constructor(id) {
        this.id = id
    }
    foo(x) {
        console.log(x)
    }
}
class Rectangle extends Shape { ..}
{% endhighlight %}
 - promise

## Redux
- Single store

{% highlight javascript %}
class Foo extends React.Component {
    constructor(props) {
        super(props)
        this.state = {count: props.initialCount}
        this.handler = this.handler.bind(this)
    }
    handler = () => {
        this.setState()
    }
    render() {
        return (
            <div onClick={this.handler}>
                Clicks: {this.state.count}
            </div>
        )
    }
}
{% endhighlight %}
