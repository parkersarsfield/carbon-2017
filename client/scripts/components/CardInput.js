import React, { Component } from 'react';

export default class CardInput extends Component {

  render() {
    const buttonLogo = this.props.isBuying ? 'fa fa-spinner fa-spin buy-icon' : 'fa fa-usd buy-icon';

    return (
      <form className="order-form" onSubmit={this.props.onBuy}>
        <div className="form-group order-form-sub">
          
            <label htmlFor="cardNumber">Card Number:</label>
            <input type="text" className="form-control" id="cardNumber" placeholder="0000 1111 2222 3333" />
            <label htmlFor="CVC">Security Code:</label>
            <input type="text" className="form-control card-number" id="CVC" placeholder="123" />
          <button className="btn buy-button">
          <i className={buttonLogo}> </i> BUY
        </button>
        </div>        
      </form>
    );
  }
}
