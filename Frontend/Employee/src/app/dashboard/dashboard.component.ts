import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { EmployeeService } from '../employee.service';

@Component({
  selector: 'app-dashboard',
  imports: [RouterModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {
  constructor(private empService:EmployeeService,private router : Router){
    }


    totalEmployees: number = 0;
    maleCount: number = 0;
  femaleCount: number = 0;
  otherCount: number = 0;
  totalDepartments:number = 0;
    ngOnInit(): void {
      this.empService.getAllEmployees().subscribe((response) =>{
        console.log(response);
        if (Array.isArray(response)) {
       this.totalEmployees = response.length; 
       this.maleCount = response.filter(emp => typeof emp.gender === 'string' && emp.gender.toLowerCase() === 'male').length;
          this.femaleCount = response.filter(emp => typeof emp.gender === 'string' && emp.gender.toLowerCase() === 'female').length;
          this.otherCount = response.filter(emp => typeof emp.gender === 'string' && emp.gender.toLowerCase() === 'other').length;
    }else{
           console.log("Error")
        }
    
       }
      )
      this.empService.getAllDepartment().subscribe((response) =>{
        console.log(response);
        if (Array.isArray(response)) {
       this.totalDepartments = response.length; 
    }else{
           console.log("Error")
        }
    
       }
      )
      
    }
  // ngOninit(){
  //   console.log('Into onInit Dash');
  //   this.empService.getAllEmployees().subscribe((response) =>{
  //     console.log(response);
  //     if(response == true){
  //       this.router.navigate(['/dashboard'])
  //     }else{
  //        console.log("Error")
  //     }
  //   }
  //   )}
  }
