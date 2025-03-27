import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { EmployeeDetailsComponent } from './employee-details/employee-details.component';

export const routes: Routes = [

    {path:'',component:LoginComponent},
    {path:'dashboard',component:DashboardComponent},
    {path:'dashboard/employeeDetails',component:EmployeeDetailsComponent}
];
