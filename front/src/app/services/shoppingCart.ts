import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { application } from '../config/application';

@Injectable({
  providedIn: 'root',
})
export class shoppingCart {

    items = [];

    constructor(private http: HttpClient, private app : application) { }
    getBaseUrl() {
        return this.app.isOnDebugMode() ? 'http://localhost:8000' : "" ;
    }

    getCartItems() {
        return this.items;
    }

    addItemToCart(item : any, qty : number) {
        var order_item = {
            item_id : item.id,
            name : item.name,
            qty : qty,
            price : item.price,
            total : item.price * qty,
            currency : item.currency
        };
        this.items.push(order_item);
        this.app.notify( item.name + " added.");
    }

    getCartTotal() {
        var total = 0;
        for (let i of this.items) {
            total += i.total;
        }
        return total;
    }

    clearCart() {
        this.items = [];
    }

    getCartItemCount() {
        return this.items.length;
    }

    getTotalCurrency(){
        if(this.items.length > 0){
            return this.items[0].currency + '.';
        }
        return '';
    }

  
}