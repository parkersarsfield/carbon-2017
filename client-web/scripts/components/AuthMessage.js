import React, { Component } from 'react';

export default class Authentication extends Component {
  
  render() {
    let message;

    if (this.props.status === 'WAIT') {
      message = 'Please perform the above gestures...';
    } else if (this.props.status === 'PASS') {
      message = 'Your order has been successfully placed!'
    } else if (this.props.status === 'FAIL') {
      message = 'Authentication failed. Try your order again.';
    }

    return <p className="alert">{message}</p>;
  }
}
