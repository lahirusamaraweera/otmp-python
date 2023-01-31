import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { Routes, RouterModule } from '@angular/router';

import { MatSliderModule } from '@angular/material/slider';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatCardModule} from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';

import { 
  FormsModule, 
  ReactiveFormsModule } from '@angular/forms';
import {MatButtonModule} from '@angular/material/button';


import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NavBarComponent } from './ui-components/nav-bar/nav-bar.component';
import { itemComponent } from './ui-components/item/item.component';
import { HttpClientModule } from '@angular/common/http';
import { SearchComponent } from './ui-components/search/search.component';
import { CartComponent } from './ui-components/cart/cart.component';
import { MatBottomSheetModule } from '@angular/material/bottom-sheet';
import { MatSnackBarModule } from '@angular/material/snack-bar';

import { ShoppingViewComponent } from './pages/shopping/shoppingView.component';

const routes: Routes = [];

@NgModule({
  declarations: [
    AppComponent,
    NavBarComponent,
    itemComponent,
    SearchComponent,
    CartComponent,
    ShoppingViewComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatSliderModule,
    MatCheckboxModule,
    MatCardModule,
    FormsModule,
    ReactiveFormsModule,
    MatButtonModule,
    MatInputModule,
    MatIconModule,
    MatBottomSheetModule,
    MatSnackBarModule,
    NgbModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
