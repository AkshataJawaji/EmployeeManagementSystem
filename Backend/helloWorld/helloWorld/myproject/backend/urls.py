# from django.urls import path
# from . import views

# urlpatterns = [
#     # Example route — adjust this based on your views
#     path('api/', views.home, name='home'),
# ]

# from django.urls import include, path
# from .views import LoginView
# from myproject.backend import views
# from . import views


# urlpatterns = [
#     #path('employees/', EmployeeAPIView.as_view(), name='employees'),
#     path('api/login/', LoginView.as_view(), name='login'),
#     path('api/', include('backend.urls')), 
    
# ]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('employees/', views.get_all_employees, name='get_all_employees'),
#     path('login/', views.LoginView.as_view(), name='login'),
# ]



# from django.urls import path
# from .views import GetEmployeeDetails, GetAllEmployees, LoginView


# urlpatterns = [
#     path('api/employee/<int:emp_id>/', GetEmployeeDetails.as_view(), name='get_employee_details'),
#     path('api/employees/', GetAllEmployees.as_view(), name='get_all_employees'),
#     path('api/login/', LoginView.as_view(), name='login'),
# ]




# from django.urls import path
# from .views import GetEmployeeDetails, LoginView

# urlpatterns = [
#     # path('api/employee/<int:emp_id>/', GetEmployeeDetails.as_view(), name='get_employee_details'),
#     path('api/employees/', GetEmployeeDetails.as_view(), name='get_employee_details'),
#     path('api/login/', LoginView.as_view(), name='login'),
# ]

# from django.urls import path
# from .views import GetEmployeeDetails,LoginView,GetAllEmployees

# urlpatterns = [
#     path('employees/',GetAllEmployees.as_view(), name='get_all_employees'),
#     path('employee/<int:emp_id>/', GetEmployeeDetails.as_view(), name='get_employee_details'),
#     path('login/', LoginView.as_view(), name='login'),
# ]


# from django.urls import path
# from .views import GetAllEmployees,GetEmployeeDetails, LoginView

# urlpatterns = [
#     path('employees/',GetAllEmployees.as_view(), name='get_all_employees'),  # <- This is missing in the error output
#     path('employee/<int:emp_id>/', GetEmployeeDetails.as_view(), name='get_employee_details'),
#     path('login/', LoginView.as_view(), name='login'),

    
# ]

# backend/urls.py
from django.urls import path
from .views import LoginView

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),  # Ensure this is correct
]
