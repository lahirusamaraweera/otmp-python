import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.css']
})
export class itemComponent implements OnInit {

  qty = 1;
  @Input()
  item

  constructor() { }

  ngOnInit(): void {
  }

}
