import React, { Component } from 'react';

export default class Authentication extends Component {

  render(){
    return (
      <div className="gestures">
        {this.props.code.map((gesture, index) => {
          return (
            <div>
              <img src={`../../images/${gesture}.png`} key={index} className="gesture" />
              <p className="gesture-label">{gesture.toUpperCase()}</p>
            </div>
            );
          }
        )}
      </div>
    );
  }
}
