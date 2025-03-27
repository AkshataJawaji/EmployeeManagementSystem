import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {

  constructor(private http: HttpClient) { }

  private baseUrl = 'http://localhost:8082/user';


  logIn(username: string, password: string): Observable<any> {
    const url = `${this.baseUrl}/logIn?userId=${username}&password=${password}`;
    return this.http.get<any>(url);
  }
  getAllEmployees():Observable<any>{
    const url = 'http://localhost:8082/getAllEmployees';
    return this.http.get<any>(url);
  }
  getAllDepartment():Observable<any>{
    const url = 'http://localhost:8082/department/getAll';
    return this.http.get<any>(url);
  }
}
