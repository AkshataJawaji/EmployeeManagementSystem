import { Component } from '@angular/core';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { EmployeeService } from '../employee.service';
import { Router, RouterModule } from '@angular/router';


@Component({
    
  selector: 'app-login',
  templateUrl:'./login.component.html',
  styleUrl: './login.component.css',
  imports :[FormsModule,ReactiveFormsModule,RouterModule]
  
})

export class LoginComponent {
  // username = '';
  // password = '';

  loginForm !: FormGroup;
  constructor(private empService:EmployeeService,private router : Router){
    this.initlizeForm();

  }

  ngOninit():void {
  // this.initlizeForm();
  }

  initlizeForm(){
    this.loginForm = new FormGroup({
      username : new FormControl(),
      password : new FormControl()
    })
  }
  submit() :void{
    // Handle sign-in logic here
    console.log("login form",this.loginForm.value)
   this.empService.logIn(this.loginForm.value.username,this.loginForm.value.password).subscribe((response) =>{
    console.log(response);
    if(response == true){
      this.router.navigate(['/dashboard'])
    }else{
       console.log("Error")
    }

   }
  )}
}

