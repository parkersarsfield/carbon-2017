import React, { Component } from 'react';

export default class Authentication extends Component {

  render(){
    return (
      <div>
        {this.props.code.map((gesture, index) => <img src={`../../images/${gesture}.png`} key={index} className="gesture" />)}
      </div>
    );
  }
}
