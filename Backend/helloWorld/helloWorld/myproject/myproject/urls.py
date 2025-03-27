# """
# URL configuration for myproject project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# # from django.contrib import admin
# # from django.urls import path

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# # ]


# from django.contrib import admin
# from django.urls import path
# from backend import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/hello/', views.hello_world, name='hello_world'),
# ]




# from django.urls import path
# from .views import get_employee, save_employee, get_all_employees, home

# urlpatterns = [
#     path('', home, name='home'),
#     path('employee/<str:id>/', get_employee, name='get_employee'),
#     path('employee/save/', save_employee, name='save_employee'),
#     path('getAllEmployees/', get_all_employees, name='get_all_employees'),
# ] 



# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('backend.urls')),  # Connect backend app routes
# ]



# from django.contrib import admin
# from django.urls import path, include

# # urlpatterns = [
# #     path('admin/', admin.site.urls),   
# #     path('api/', include('backend.urls')),   # Include the backend app URLs
# # ]

# urlpatterns = [
#     path('api/employees/', GetAllEmployees.as_view(), name='get_all_employees'),
#     path('api/login/', LoginView.as_view(), name='login'),
# ]





# from django.urls import path
# # from .views import GetAllEmployees, LoginView # type: ignore
# from backend.views import GetAllEmployees, LoginView


# urlpatterns = [
#     # path('api/employee/<int:emp_id>/', GetEmployeeDetails.as_view(), name='get_employee_details'),
#     path('api/employees/', GetAllEmployees.as_view(), name='get_all_employees'),
#     path('api/login/', LoginView.as_view(), name='login'),
# ]
# 



# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('backend.urls')),
# ]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),  # Make sure to include the app's URLs
]

