import { Component, OnInit, Input } from '@angular/core';
import { shoppingCart } from '../../services/shoppingCart';

@Component({
  selector: 'item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.css']
})
export class itemComponent implements OnInit {

  qty = 1;
  @Input()
  item

  constructor(private shoppingCart : shoppingCart) { }

  ngOnInit(): void {
  }

  addtoCart() :void {
    this.shoppingCart.addItemToCart(this.item, this.qty);
  }

}
