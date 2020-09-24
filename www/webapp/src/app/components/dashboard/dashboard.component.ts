import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/shared/services/auth.service';
import { HttpClient } from '@angular/common/http';

import { createChart } from 'lightweight-charts';



@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  n50bc: any;
  n50nextbc: any;
  field:any;
  rem: any;
  jbody: any;
  

  constructor(public authService: AuthService, private httpClient: HttpClient) { }

  ngOnInit(): void {


  }

  
  get_n50_bc(){
    this.n50nextbc = ""
    
   
    this.httpClient.get('http://localhost:3000/n50bc').subscribe((data)=>{
      this.n50bc = data;
        // console.log(data);
        this.rem = "remove";
        console.log(this.n50bc);
        
    });
}


get_n50_next_bc(){
  this.n50bc = ""
  this.rem = "remove";
    
    
   
  this.httpClient.get('http://localhost:3000/n50nextbc').subscribe((data)=>{
    this.n50nextbc = data;
      console.log(data);
      console.log(this.n50nextbc);
      
  });
}


get_candlestick(){
  // this.n50bc = ""  
   this.jbody = {
     "pattern" : "marubozu"
   }
  this.httpClient.get('http://localhost:3000/candlestick/'+this.jbody).subscribe((data)=>{
    this.n50nextbc = data;
      console.log(data);
      console.log(this.n50nextbc);
      
  });
}

}
