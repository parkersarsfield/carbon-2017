import React, { Component } from 'react';

export default class Header extends Component {
  render() {
    return (
      <div className="header">
        <h1>Bio Authentication Webstore</h1>
        <img src="/images/caplogo.png" className="logo"/>
        <hr />
      </div>
    );
  }
}
