import React, { Component } from 'react';

export default class AuthLoaded extends Component {
  render() {
    let iconClass;

    if (this.props.status === 'WAIT') {
        iconClass = 'fa fa-spinner fa-spin fa-5x wait';
    } else if (this.props.status === 'PASS') {
      iconClass = 'fa fa-check fa-5x pass';
    } else if (this.props.status === 'FAIL') {
      iconClass = 'fa fa-times fa-5x fail';
    }

    return (
      <div className="loading-area">
        <i className={iconClass} />
      </div>
    );
  }
}
