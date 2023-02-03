import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { ShoppingViewComponent } from './pages/shopping/shoppingView.component';


const routes: Routes = [
  {
    path : '', component : ShoppingViewComponent
  },
  {
    path : 'login', component : LoginComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
