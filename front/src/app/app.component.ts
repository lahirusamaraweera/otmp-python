import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatCheckboxModule} from '@angular/material/checkbox';
import { ItemService } from './services/app.service';

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

  constructor(private ItemService: ItemService) { }
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

  ngOnInit() {
    this.getItems();
  }

}
