import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class BackendService {

  constructor(private httpClient: HttpClient) { }

  public get(){  
    return this.httpClient.get("http://35.200.139.5:3000/influx");  
    }  

    
}
