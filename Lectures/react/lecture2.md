# Pretty React Components + RESTful API Requests

## Material UI
There are many pre-built react components (e.g. buttons, sliders, menu bars, etc) that you can use to build core pieces of your application. Since these are just react components (just like the kind you wrote) -- they're easy to reason about and use. They usually take props for input. A useful component library is Material UI, which can be found [here](https://material-ui-next.com/). Here are some examples for the Material UI [buttons](https://material-ui-next.com/demos/buttons/). 

We will see and incoporate this library in class, and code will be uploaded after lecture.

## RESTful API Requests via axios
[Axios](https://www.npmjs.com/package/axios) is a javascript library used to make RESTful API requests (just like the `requests` library we used in python). 

The typical pattern for making RESTful API requests in a component goes something like this: we want to trigger a function that will make the RESTful API request. It may take some time to complete. When it finishes and the response data has arrived, we would want to trigger an _update to state_ by calling `this.setState` with some part of the data. Once the state of the component is updated with the data that has arrived, the component will re-render automatically and the new state may affect the view based on what we've written. 

A minimal example is below. Clicking on this component will cause a request to be fired off which will then end up populating the 
component with the response data for the `GET http://adpl.suyash.io/api/sites` request.

```js
class DisplayData extends React.Component {
  constructor() {
    super(); // call superclass constructor
    this.state = {
      "data": "Nothing yet", // initial state
    };
  }
  
  fetchData = () => {
    axios.get("http://adpl.suyash.io/api/sites").then( (response) => { 
      // this is called once the request has finished and response data is present:
      console.log(response.status); // print status code
      this.setState({"data": response.data}); // update the component's state
    });
  }

  render() {
    return (
      <div onClick={this.fetchData}>
        {this.state.data} 
      </div>
    )
  }
  
}
```

## React component styles
Advanced styling covered in class.
