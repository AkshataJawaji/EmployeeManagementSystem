# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response

# # @api_view(['GET'])
# # def hello_world(request):
# #     return Response({"message": "Hieeeeeeeeeeeeeeeeee"})


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
# from django.core.exceptions import ObjectDoesNotExist
# from .models import Employee
# from .services import add_employee, get_all_employees, find_employee_by_id

# try:
#     from.services import add_employee, get_all_employees, find_employee_by_id
# except ImportError as e:
#     print(f"ImportError: {e}")

# import json

# @csrf_exempt
# def get_employee(request, id):
#     if request.method == 'GET':
#         try:
#             employee = find_employee_by_id(id)
#             return JsonResponse({
#                 'id': str(employee.id),
#                 'name': employee.name,
#                 'age': employee.age,
#                 'gender': employee.gender,
#                 'company': employee.company,
#                 'location': employee.location,
#                 'job_type': employee.job_type,
#                 'date_of_joining': employee.date_of_joining,
#                 'department': employee.department.name if employee.department else None
#             })
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=404)

# @csrf_exempt
# def save_employee(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             employee = add_employee(data)
#             return JsonResponse({'message': 'Employee added successfully', 'id': str(employee.id)})
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

# @csrf_exempt
# def get_all_employees(request):
#     if request.method == 'GET':
#         employees = get_all_employees()
#         employee_list = [
#             {
#                 'id': str(emp.id),
#                 'name': emp.name,
#                 'age': emp.age,
#                 'gender': emp.gender,
#                 'company': emp.company,
#                 'location': emp.location,
#                 'job_type': emp.job_type,
#                 'date_of_joining': emp.date_of_joining,
#                 'department': emp.department.name if emp.department else None
#             }
#             for emp in employees
#         ]
#         return JsonResponse(employee_list, safe=False)

# def home(request):
#     return JsonResponse({'message': 'Welcome to the Employee Project!'})







# from .models import Employee, Department
# from django.core.exceptions import ObjectDoesNotExist



# def add_employee(data):
#     try:
#         existing_emp = Employee.objects.get(name=data['name'])
#         raise Exception("Employee Already Exists")
#     except ObjectDoesNotExist:
#         pass

#     department = None
#     if 'department' in data and data['department']:
#         department_name = data['department'].get('name')
#         department, created = Department.objects.get_or_create(name=department_name)

#     employee = Employee.objects.create(
#         name=data['name'],
#         age=data['age'],
#         gender=data['gender'],
#         company=data['company'],
#         location=data['location'],
#         job_type=data['job_type'],
#         date_of_joining=data['date_of_joining'],
#         department=department
#     )
#     return employee






# from django.contrib.auth.hashers import check_password
# from django.views import View
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Employee, Login
# from .serializers import EmployeeSerializer, LoginSerializer,
# from django.http import JsonResponse
# from .models import Employee

# class GetAllEmployees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)



# class GetEmployeeDetails(APIView):
#     def get(self, request):
#         queryset = Employee.objects.all()
#         records = list(queryset.values())
#         return Response(records, 200)


# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get("email")
#         password = request.data.get("password")



#         try:
#             user = Login.objects.get(email=email)
            
#             # Check if the provided password matches (assuming passwords are stored in plaintext)
#             if user.password == password:  # If using hashed passwords, use check_password(password, user.password)
#                 return Response(
#                     {"message": "Login Successful", "user_id": user.user_id, "name": user.name, "email": user.email},
#                     status=status.HTTP_200_OK
#                 )
#             else:
#                 return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

#         except Login.DoesNotExist:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        

        
#start
# from django.contrib.auth.hashers import check_password
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Employee, Login
# from .serializers import EmployeeSerializer, LoginSerializer
# from django.http import JsonResponse
# from backend.models import Employee



# class GetAllEmployees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         print(serializer.data)  # Debug log
#         return Response(serializer.data, status=status.HTTP_200_OK)




# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get("email")
#         password = request.data.get("password")

#         try:
#             user = Login.objects.get(email=email)
            
#             # Use hashed password check if passwords are hashed
#             if check_password(password, user.password):
#                 return Response(
#                     {"message": "Login Successful", "user_id": user.user_id, "name": user.name, "email": user.email},
#                     status=status.HTTP_200_OK
#                 )
#             else:
#                 return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

#         except Login.DoesNotExist:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#end

#commented

# class GetAllEmployees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class GetEmployeeDetails(APIView):
#     def get(self, request):
#         queryset = Employee.objects.all()
#         records = list(queryset.values())
#         return Response(records, status=status.HTTP_200_OK)

#comentted




from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Login

class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = Login.objects.get(email=email)

            # Handle plain text or hashed passwords
            if user.password == password or check_password(password, user.password):
                return Response(
                    {
                        "message": "Login Successful",
                        "user_id": user.id,
                        "name": user.name,
                        "email": user.email
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        except Login.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
