import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SignInComponent } from './components/sign-in/sign-in.component';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { ForgotPasswordComponent } from './components/forgot-password/forgot-password.component';
import { VerifyEmailComponent } from './components/verify-email/verify-email.component';
import { HomeComponent } from './components/home/home.component';
import { ChartingComponent } from './components/charting/charting.component';
import { AuthGuard } from './shared/guard/auth.guard';

import { ListComponent } from './components/list/list.component';


const routes: Routes = [
  //{ path: '', redirectTo: '/home', pathMatch: 'full'},
  { path: '', component: HomeComponent},
  { path: 'home', component: HomeComponent},
  { path: '', redirectTo: '/sign-in', pathMatch: 'full'},
  { path: 'sign-in', component: SignInComponent},
  { path: 'register-user', component: SignUpComponent},
  // { path: 'dashboard', component: DashboardComponent, canActivate: [AuthGuard]},
  { path: 'dashboard', component: DashboardComponent},
  { path: 'list', component: ListComponent},
  { path: 'forgot-password', component: ForgotPasswordComponent},
  { path: 'verify-email-address', component: VerifyEmailComponent},
  { path: 'charting', component: ChartingComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
