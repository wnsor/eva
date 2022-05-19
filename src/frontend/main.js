
import React from "react";


const myHeading = document.querySelector('h1');
myHeading.textContent = 'Hello world!';



class HelloMessage extends React.Component {
  render() {
    return <div>Hello {this.props.name}</div>;
  }
}

root.render(<HelloMessage name="Taylor" />);


const config = {
  type: 'line',
  data: data,
  options: {}
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<h1>Hello, world!</h1>);