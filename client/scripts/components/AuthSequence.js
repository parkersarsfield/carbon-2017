import React, { Component } from 'react';

export default class Authentication extends Component {

  render(){
    
    return (
      <div className="gestures">
        {this.props.code.map((gesture, index) => {
          let cls;

          if (this.props.status === 'WAIT') {
            cls = this.props.completed === index ? 'gesture' : 'gesture completed';
            cls = this.props.completed < index ? 'gesture future' : cls;
          } else if (this.props.status === 'FAIL:SOFT'){
            cls = this.props.completed === index ? 'gesture retry fail-shake' : 'gesture completed';
            cls = this.props.completed < index ? 'gesture future' : cls;
          } else if (this.props.status === 'FAIL:HARD') {
            cls = 'gesture failed fail-shake-hard';
          } else if (this.props.status === 'PASS'){
            cls = 'gesture completed';
          }

          return (
            <div key={index}>
              <img src={`../../images/${gesture}.png`} className={cls} />
              <p className="gesture-label">{gesture.toUpperCase()}</p>
            </div>
            );
          }
        )}
      </div>
    );
  }
}
