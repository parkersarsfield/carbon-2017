import React, { Component } from 'react';

export default class CardInput extends Component {

  render() {
    const buttonLogo = this.props.isBuying ? 'fa fa-spinner fa-spin' : 'fa fa-usd';

    return (
      <form className="order-form" onSubmit={this.props.onBuy}>
        <div className="form-group order-form-sub">
          <span>
            <label htmlFor="cardNumber">Enter Card Number</label>
            <input type="text" className="form-control" id="cardNumber" placeholder="0000 1111 2222 3333" />
            <label htmlFor="CVC">Enter Security Code</label>
            <input type="text" className="form-control card-number" id="CVC" placeholder="123" />
          </span>
          <button className="btn btn-primary buy-button">
          <i className={buttonLogo}> </i> Buy
        </button>
        </div>        
      </form>
    );
  }
}
