import React from 'react';
import Hello from './Hello.js';
import Counter from './Counter.js'; 
import FetchData from './FetchData.js';
import AppBar from 'material-ui/AppBar';
import TextFieldExample from './TextFieldExample.js';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
import TableExample from './TableExample.js';

var styles = {
	"appBarStyle": {
		"marginBottom": "10px",
	}
}

class App extends React.Component {
 	constructor() {
 		super();
		this.state = {
			"tableData": [
				[60, "1pm"],
				[100, "2pm"],
				[120, "3pm"],
			],
		}
 	}

	onTextFieldButtonClick = (textFieldValue) => {
		// WE HAVE THE CHILD DATA IN APP.JS YAY
		// now let's make a GET request and put result in state
		this.setState({"textFieldValueAtButtonPress": textFieldValue});
	}
 
  // One thing every component must do: 
  // define the render method
  // (this defines the view of the component)
  render() {
    return (
      <div>
	    <AppBar position="static" style={styles.appBarStyle}>
			<Toolbar>
				<Typography variant="title" color="inherit">
					Sample App	
				</Typography>
			</Toolbar>
		</AppBar>
		<Hello name="Suyash" color="red"/>
		<Hello name="Mark" />
		<Counter name="Suyash"/>
		<Counter name="Mark"/>
		<FetchData />

		<TextFieldExample onClickButton={this.onTextFieldButtonClick}/>

		<TableExample tableData={this.state.tableData} heading={["HR", "Time"]}/>
      </div>
    );
  }
}

export default App;
