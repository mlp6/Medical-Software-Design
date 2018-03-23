import React from 'react';

class Counter extends React.Component {
	// this is the class __init__
	constructor() {
		super();
		this.state = {
			"count": 0,	
		};
	}

	incrementCount = () => {
		// increment the count
		// do NOT do this.state.count = this.state.count + 1
		this.setState({"count": this.state.count + 1});
	}

	render() {
		return (
			<div onClick={this.incrementCount}>
				{this.props.name}'s count is {this.state.count} 
			</div>
		)
	}
}

export default Counter;
