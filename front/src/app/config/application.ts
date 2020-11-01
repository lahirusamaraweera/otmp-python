import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Action } from 'rxjs/internal/scheduler/Action';


@Injectable({
  providedIn: 'root',
})
export class application {

    // configurations
    IS_ON_DEBUG = !environment.production;
    constructor(private _snackBar : MatSnackBar) { }

    isOnDebugMode() {
        return this.IS_ON_DEBUG ;
    }

    notify(message:string, action :string = 'Dismiss') : void {
      this._snackBar.open(message, action, {
        duration : 5000
      });
    }

}