import React, { Component } from 'react';
import AuthLoaded from './AuthLoaded';
import AuthMessage from './AuthMessage';
import AuthSequence from './AuthSequence';

export default class Authentication extends Component {
  render() {
    const code = this.props.code;

    return code ? 
    (
        <div className="gesture-sequence">
          <AuthSequence code={this.props.code} />
          <AuthLoaded status={this.props.status} />
          <AuthMessage status={this.props.status} />
        </div>
    ) :
    null;
  }
}
