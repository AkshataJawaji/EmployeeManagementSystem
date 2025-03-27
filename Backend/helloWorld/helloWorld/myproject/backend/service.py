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

# def get_all_employees():
#     return Employee.objects.all()

# def find_employee_by_id(emp_id):
#     try:
#         return Employee.objects.get(id=emp_id)
#     except Employee.DoesNotExist:
#         raise Exception("Employee not found")




from .models import Employee, Department
from django.core.exceptions import ObjectDoesNotExist



def add_employee(data):
    try:
        existing_emp = Employee.objects.get(name=data['name'])
        raise Exception("Employee Already Exists")
    except ObjectDoesNotExist:
        pass

    department = None
    if 'department' in data and data['department']:
        department_name = data['department'].get('name')
        department, created = Department.objects.get_or_create(name=department_name)

    employee = Employee.objects.create(
        name=data['name'],
        age=data['age'],
        gender=data['gender'],
        company=data['company'],
        location=data['location'],
        job_type=data['job_type'],
        date_of_joining=data['date_of_joining'],
        department=department
    )
    return employee
