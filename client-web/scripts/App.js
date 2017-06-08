import React, { Component } from 'react';
import Header from './components/Header';
import CardInput from './components/CardInput';
import Authentication from './components/Authentication';
import 'whatwg-fetch';

export default class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      code: ['left', 'fist', 'open'],
      status: 'wait',
      isBuying: false,
    }
  }

  checkForValidation(id, count, countLimit) {
    fetch('http://172.20.10.3:5000/api/check/' + id).then(function(response) {
      console.log(response);
      if(count < countLimit)
        setTimeout(checkForValidation, 500, id, count++, count); 
    });
  }

  onBuy(event) {
    event.preventDefault();

    this.setState({
      isBuying: true,
    });
    let self = this;
    fetch('http://warm-spire-75113.herokuapp.com/api/authenticate')
    .then(function(response) {
      console.log(response);
      this.setState({ isBuying: false });
      checkForValidation(response.id);
    }).catch(function(err){
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
