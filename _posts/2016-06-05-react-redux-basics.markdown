---
layout: post
title:  "React/Redux basics"
date:   2016-06-05 16:12:22 -0800
categories: react redux
---

# ES6 Primer
Some ES6 new features that I think are immediately useful:

 - variable declaraton: `const`, `let`
 - arrow function:
{% highlight javascript %}
    const getName = (item) => { return item.name } 
{% endhighlight %}
 - property shorthand:
{% highlight javascript %}
    obj = {name, score} // === obj = {name:name, score:score}
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
// class extension
class Rectangle extends Shape { ..}
{% endhighlight %}
 - promise

For a complete list see <http://es6-features.org/>.

## Redux Basics
- Single store
- Reducers: (state, action) -> new state They don't mutate previous state. Instead they return new states each time.
- Action: payload of data. only source of information to store
- Component: UI component. Define how things look. example is a Todo component
- Container: define how things work. example is how AddTodo works

Data flow:
`container dispatches action --> store --> reducers --> store --> components`

## Redux Implementation
- Store:
{% highlight javascript %}
const App = () => (
  <div>
    //reducers or components
    <AddTodo />
    <Footer />
  </div>
)

let store = createStore(todoApp)

render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
)
{% endhighlight %}
- Action:
{% highlight javascript %}
export const addTodo = (text) => {
  return {
    type: 'ADD_TODO',
    id: nextTodoId++,
    text
  }
}
{% endhighlight %}
- Reducer:
{% highlight javascript %}
const todo = (state = [], action) => {
    switch(action.type) {
        case 'ADD_TODO':
            return [
                ...state,
                {id: action.id, text:action.text}
            ]
        case 'DELETE_TODO':
            ...
        default:
            return state
    }
}
{% endhighlight %}
- component
{% highlight javascript %}
const TodoList = ({ todos, onTodoClick }) => (
  <ul>
    {todos.map(todo =>
      <Todo
        key={todo.id}
        {...todo}
        onClick={() => onTodoClick(todo.id)}
      />
    )}
  </ul>
)

TodoList.propTypes = {
    ...
}

{% endhighlight %}
- container
{% highlight javascript %}
const getVisibleTodos = (todos, filter) => {
  switch (filter) {
    ...
  }
}

const mapStateToProps = (state) => {
  return {
    todos: getVisibleTodos(state.todos, state.visibilityFilter)
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onTodoClick: (id) => {
      dispatch(toggleTodo(id))
    }
  }
}

const VisibleTodoList = connect(
  mapStateToProps,
  mapDispatchToProps
)(TodoList)

export default VisibleTodoList
{% endhighlight %}
- connecting components to containers 
{% highlight javascript %}
const TodoContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(TodoComponent)
{% endhighlight %}
Here we have `mapStateToProps` that converts from state to connected component props, and `mapDispatchToProps` that dispatches actions to connected component's props

