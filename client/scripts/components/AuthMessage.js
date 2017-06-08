import React, { Component } from 'react';

export default class Authentication extends Component {
  
  render() {
    let message;

    if (this.props.status === 'WAIT') {
      message = 'Please perform the above gestures...';
    } else if (this.props.status === 'PASS') {
      message = 'Your order has been successfully placed!'
    } else if (this.props.status === 'FAIL:HARD') {
      message = 'Gesture authentication failed.';
    } else if (this.props.status === 'FAIL:SOFT') {
      message = 'Last gesture incorrect, try it again.'
    }

    return <p className="alert">{message}</p>;
  }
}
