import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatCheckboxModule} from '@angular/material/checkbox';
import { ItemService } from './services/app.service';
import { Pipe, PipeTransform } from '@angular/core';
import { MatBottomSheet, MatBottomSheetRef } from '@angular/material/bottom-sheet';
import { CartComponent } from './ui-components/cart/cart.component';
import { shoppingCart } from './services/shoppingCart';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
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
        .subscribe(itmes => {
          this.items  = <any>itmes;
        });
  }

  showCart(): void {
    this._bottomSheet.open(CartComponent);
  }

  getCartItemCount() {
    return this.shoppingCart.getCartItemCount();
  }

}
