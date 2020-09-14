import { Component, OnInit } from '@angular/core';

//import { BackendService } from '../../backend.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  SERVER_URL = "http://35.200.139.5:3000/influx";
  uploadForm: FormGroup;  
  sym: string = "";
  data1 : any;
  data2 : any;
  data3 : any;
  data4 : any;

  data = [];
  msg : any;
  heading : any;
  market : any;
  


  constructor(private formBuilder: FormBuilder, private httpClient: HttpClient) { 

    

  }

  ngOnInit() {

    
    this.httpClient.get('http://35.200.139.5:3000/topgainer/').subscribe((data)=>{
      this.data3 = data[0];
        console.log(this.data3);
        
    });

    
    
    this.httpClient.get('http://35.200.139.5:3000/toploser/').subscribe((data)=>{
      this.data4 = data[0];
        console.log(this.data4);
        
    });




    
  }

  get_ric_data(sym){
    this.heading = "STOCK ACTION";
    this.market = "NSE";
   
    this.httpClient.get('http://35.200.139.5:3000/influx/'+sym).subscribe((data)=>{
      this.data1 = data[0];
        console.log(this.data1);
        
    });
    this.get_sym_detail(sym);
}

get_sym_detail(s){

  this.httpClient.get('http://35.200.139.5:3000/detail/'+s).subscribe((data)=>{
    this.data2 = data[0];
      console.log(this.data2);
      
  });

}


  // get_ric_data(sym) {
  //   console.log(sym);
  //   this.backendService.get().subscribe((ret: any[])=>{  
  //     console.log(ret);  
  //     this.data = ret;  
  //     })  

  // }

}
