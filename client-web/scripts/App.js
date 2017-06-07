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
      status: 'fail',
      isBuying: false,
    }
  }

  onBuy(event) {
    event.preventDefault();

    this.setState({
      isBuying: true,
    });

    fetch('http://172.20.10.3:5000/api/authenticate').then(function(response) {
      console.log(response);
    });

    
    /*request({
      url: '192.168.17.213:5000/api/authenticate',
      method: 'GET',
      data: {
      }}, function(err, res, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(res);
          console.log(body);
        }

        this.setState({ isBuying: false });
    });

    setTimeout(() => {
      this.setState({
        code: ['left','fist', 'open'],
        status: 'fail',
        isBuying: false,
      });
    }, 1000);*/
    
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
