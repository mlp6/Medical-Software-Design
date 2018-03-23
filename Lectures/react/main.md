# ReactJS Frontend Applications Introduction

[ReactJS](https://reactjs.org/) is a Javascript framework written by Facebook to make it easy to build applications with a Graphical User Interface on the web. You can think of web applications just like any application that runs on your computer with a GUI -- except that it runs inside a browser (but still "on" your computer). When you visit a web URL of a react application, such as [http://adpl.suyash.io](http://adpl.suyash.io), your browser actually _downloads_ the code and assets needed to run the web application to your computer and then runs the web application (again, this is all running on _your_ computer). One of the biggest advantages of web applications is that they are cross platform, because browsers generally run the same across Windows/Mac/Linux and mobile devices like iPhone/Android. 

We will cover how to setup React locally next class, but if you want to play around before then, you can use a cloud IDE like stackblitz here: https://stackblitz.com/fork/react 

## Basic HTML/JSX primer
HTML is a markup language that can have nested tag structures like so:
```html
<html>
	<div>
	Hello, world
	</div>
</html>
```
The `<div>` tag is just a container that holds other containers or text. This means you can have nested `<div>`s like so:

```
<div>
I am the parent div, but there can also be a child div encapsulated inside of me:
	<div>
		I'm the child div container
	</div>
</div>
```

In React/JSX, we have components which are just like HTML tags. These components may render buttons, text, or really any view that also has some functionality. Often times React components are "self closing" tags that don't contain children and look like `<Component />` For example:

```
<div>
	<Hello />
</div>
```
Plops the `Hello` component and any of it's functionality right there on the screen. We can plop another one right below it like so:
```
<div>
	<Hello />
	<Hello />
</div>
```

## Anatomy of a React Application
### Components
A component is a key unit of React--it is the most granular unit that has _both_ functionality and a view. Components are classes in Javascript that inherit from a base class `React.Component` that imbue your class with additional React-rendering powers. Every component has to do one thing -- define a `render()` method that returns a blob of `JSX` which is essentially `HTML` with some minor changes that we will see. 

```js
// Hello.js:
import React from 'react';

class Hello extends React.Component {

	render() {
		return (
			<div>
				Hello, Suyash
			</div>
		)
	}

}

export default Hello; // this allows the Hello class to be available to other modules importing this file
```
If we render this as the only thing inside our `App` component (which is the "root" component), the browser will show one line: "Hello, Suyash" -- we will see this in class (and you can see it in the example code that will be pushed after class).

