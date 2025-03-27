// src/app/app.module.ts

import { NgModule } from '@angular/core';
import { BrowserModule, platformBrowser } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';  // For ngModel (Two-way binding)

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { EmployeeService } from './employee.service';

@NgModule({
    declarations: [
     
    ],
    imports: [
      BrowserModule,    // Required for browser-based Angular apps
      FormsModule,       // Import FormsModule for ngModel (two-way data binding)
      AppComponent,     // Root component
      // LoginComponent,
      FormsModule,
      BrowserAnimationsModule,
      ReactiveFormsModule,
    ],
    providers: [EmployeeService],
    bootstrap: [] // Bootstrap with the root component (AppComponent)
  })
export class AppModule { }
platformBrowser().bootstrapModule(AppModule);
