import { Component } from '@angular/core';
import { Chart } from 'Chart.js';

interface Employee {
  gender: string;
  status: string;
  employeeId: number;
  deviceEnrollId: string;
  employeeName: string;
  company: string;
  location: string;
  jobType: string;
  department: string;
  destination: string;
  employeeType: string;
  dateOfJoining: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title(title: any) {
    throw new Error('Method not implemented.');
  }
  employees: Employee[] = [
    // ... your employee data here
  ];

  searchKeyword = '';

  onboardingCount = 0;
  activeCount = 0;
  resignedCount = 0;
  abscondedCount = 0;

  ngOnInit() {
    // Calculate counts
    this.onboardingCount = this.employees.filter(employee => employee.status === 'Onboarding').length;
    this.activeCount = this.employees.filter(employee => employee.status === 'Active').length;
    this.resignedCount = this.employees.filter(employee => employee.status === 'Resigned').length;
    this.abscondedCount = this.employees.filter(employee => employee.status === 'Absconded').length;

    // Create gender distribution chart
    const ctx = document.getElementById('genderChart') as HTMLCanvasElement;
    const genderChart = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: ['Male', 'Female', 'Others'],
        datasets: [{
          data: [this.employees.filter(employee => employee.gender === 'Male').length,
            this.employees.filter(employee => employee.gender === 'Female').length,
            this.employees.filter(employee => employee.gender === 'Others').length],
          backgroundColor: ['#3e95cd', '#8e5ea2', '#3cba94'],
        }]
      }
    });
  }

  get filteredEmployees(): Employee[] {
    return this.employees.filter(employee =>
      employee.employeeName.toLowerCase().includes(this.searchKeyword.toLowerCase())
    );
  }
}