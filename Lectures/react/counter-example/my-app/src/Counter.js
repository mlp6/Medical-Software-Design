import React from 'react';
import Button from 'material-ui/Button';

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
			<div>
				<Button variant="raised" onClick={this.incrementCount}>
				{this.state.count}
				</Button>
			</div>
		)
	}
}

export default Counter;
