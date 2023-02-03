import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { application } from '../config/application';

@Injectable({
  providedIn: 'root',
})
export class ItemService {

  constructor(private http: HttpClient, private app : application) { }

  getBaseUrl() {
    return this.app.isOnDebugMode() ? 'http://localhost:8000' : "" ;
  }

  getItems() {
      var url = this.getBaseUrl() + '/api/items';
      return this.http.get(url);
  }

  getCategories() {
      var url = this.getBaseUrl() + '/api/categories';
      return this.http.get(url);
  }

  searchItemsByName(name:string) {
      var url = this.getBaseUrl() + '/api/items?name=' + name;
      return this.http.get(url);
  }
}