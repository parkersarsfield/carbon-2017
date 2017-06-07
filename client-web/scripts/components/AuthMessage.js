import React, { Component } from 'react';

export default class Authentication extends Component {
  
  render() {
    let message;

    if (this.props.status === 'wait') {
      message = 'Please perform the above gestures...';
    } else if (this.props.status === 'pass') {
      message = 'Your order has been successfully placed!'
    } else if (this.props.status === 'fail') {
      message = 'Authentication failed. Try your order again.';
    }

    return <p className="alert">{message}</p>;
  }
}
