import React, { Component } from 'react';
import Header from './components/Header';
import CardInput from './components/CardInput';
import Authentication from './components/Authentication';
import 'whatwg-fetch';

export default class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      code: null,
      status: 'WAIT',
      isBuying: false,
    }
  }

  checkForValidation(id) {
    let self = this;

    setTimeout(function(){
      fetch('http://warm-spire-75113.herokuapp.com/api/check?transaction_id=' + id)
      .then(function(response){
        return response.json();
      })
      .then(function(json) {
        if (json.status === 'WAIT') {
          self.checkForValidation(id);
        } else {
          console.log('other stuff here');
          self.setState({
            status: json.status,
          });
        }
      });
    }, 1000);
  }

  onBuy(event) {
    event.preventDefault();

    this.setState({
      isBuying: true,
    });

    let self = this;

    fetch('http://warm-spire-75113.herokuapp.com/api/authenticate')
    .then(function(response) {
      return response.json();
    }).then(function(json) {
      console.log(json);
      self.setState({
        code: [json.gesture_one, json.gesture_two, json.gesture_three],
        status: 'WAIT',
        isBuying: false,
      });

      self.checkForValidation(json.transaction_id, 0)
    })
    .catch(function(err){
      console.log(err);
      self.setState({ isBuying: false });
    });
  }

  render() {
    return (
      <div className="container">
        <Header />
        <div className="order-container">
          <CardInput onBuy={this.onBuy.bind(this)} isBuying={this.state.isBuying}/>
        </div>
        <Authentication code={this.state.code} status={this.state.status}/>
      </div>
    );
  }
}
