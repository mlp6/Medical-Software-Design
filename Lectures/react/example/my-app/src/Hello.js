import React from 'react';

const default_color = "green";

class Hello extends React.Component {
	render() {
		
		var color = this.props.color;
		if (color === undefined) {
			color = default_color;
		}

		return (
		<div style={ {'color': color} }>
			Hello there {this.props.name}
		</div>
		);
	}
}

export default Hello;
