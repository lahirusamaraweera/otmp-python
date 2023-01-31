import { Component } from '@angular/core';
import { ItemService } from '../../services/app.service';
import { MatBottomSheet, MatBottomSheetRef } from '@angular/material/bottom-sheet';
import { CartComponent } from '../../ui-components/cart/cart.component';
import { shoppingCart } from '../../services/shoppingCart';


@Component({
  selector: 'shopping-view',
  templateUrl: './shoppingView.component.html',
  styleUrls: ['./shoppingView.component.css']
})

export class ShoppingViewComponent {
  title = 'my-app';
  slider_val = 10;
  checked = false;
  indeterminate = false;
  labelPosition: 'before' | 'after' = 'after';
  disabled = false;
  items = [];
  categories = [];
  filter = null;
  filterargs = {title: 'hello'};


  constructor(
    private ItemService: ItemService, 
    private _bottomSheet: MatBottomSheet,
    private shoppingCart : shoppingCart ) { 
    }

  getItems(): void {
    this.ItemService.getItems()
        .subscribe(itmes => {
          this.items  = <any>itmes;
        });
    this.ItemService.getCategories()
        .subscribe(categories => {
            this.categories = <any>categories;
        });
  }

  getItemFilterArg() {
    return { name: this.filter };
  }

  ngOnInit() {
    this.getItems();
  }

  save(event) {
    this.ItemService.searchItemsByname(event.target.value)
        .subscribe(items => {
          this.items  = <any>items;
        });
  }

  showCart(): void {
    this._bottomSheet.open(CartComponent);
  }

  getCartItemCount() {
    return this.shoppingCart.getCartItemCount();
  }

}
