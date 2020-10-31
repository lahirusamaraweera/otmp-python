import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { itemComponent } from './item.component';

describe('itemComponent', () => {
  let component: itemComponent;
  let fixture: ComponentFixture<itemComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ itemComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(itemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
