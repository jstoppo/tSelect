import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/shared/services/auth.service';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  n50bc: any;

  constructor(public authService: AuthService, private httpClient: HttpClient) { }

  ngOnInit(): void {
  }

  
  get_n50_bc(){
    
   
    this.httpClient.get('http://localhost:3000/n50bc').subscribe((data)=>{
      this.n50bc = data;
        console.log(data);
        console.log(this.n50bc);
        
    });
}

}
