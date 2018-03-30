import React from 'react';
import Hello from './Hello.js';
import Counter from './Counter.js'; 
import FetchData from './FetchData.js';
import AppBar from 'material-ui/AppBar';
import TextFieldExample from './TextFieldExample.js';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';

var styles = {
	"appBarStyle": {
		"marginBottom": "10px",
	}
}

class App extends React.Component {
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
		<TextFieldExample />
      </div>
    );
  }
}

export default App;
