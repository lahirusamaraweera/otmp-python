import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class application {

    // configurations
    IS_ON_DEBUG = !environment.production;
    constructor() { }

    isOnDebugMode() {
        return this.IS_ON_DEBUG ;
    }

}