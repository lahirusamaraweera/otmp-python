import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { application } from '../config/application';

@Injectable({
  providedIn: 'root',
})
export class shoppingCart {

    items = []
    constructor(private http: HttpClient, private app : application) { }


    getCartItems() {
        return this.items;
    }

    addItemToCart(item : object) {
        this.items.push(item);
    }

    getBaseUrl() {
        return this.app.isOnDebugMode() ? 'http://localhost:8000' : "" ;
    }

  
}