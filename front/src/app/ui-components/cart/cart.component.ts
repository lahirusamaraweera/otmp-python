import { Component, OnInit } from '@angular/core';
import { MatBottomSheet, MatBottomSheetRef } from '@angular/material/bottom-sheet';
import { application } from '../../config/application';
import { shoppingCart } from './../../services/shoppingCart';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {

  constructor(
    private _bottomSheetRef: MatBottomSheetRef<CartComponent>,
    private _shoppingCart:shoppingCart
    ){}

  ngOnInit(): void {
  }

  close(): void {
    this._bottomSheetRef.dismiss();
  }

  getItemCount() {
    return this._shoppingCart.getCartItemCount();
  }

  getCartItems() {
    return this._shoppingCart.getCartItems();
  }

  isEmptyCart() {
    return 0 == this.getCartItems().length;
  }

  getCartTotal(){
    return this._shoppingCart.getCartTotal();
  }

  getTotalCurrency() {
    return this._shoppingCart.getTotalCurrency();
  }

  removeItemFromCart(index) {
    this._shoppingCart.removeCartItem(index);
  } 

}
