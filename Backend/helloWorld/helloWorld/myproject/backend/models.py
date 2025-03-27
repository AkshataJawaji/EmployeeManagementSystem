# from django.db import models

# class Employee(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     department = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# from django.db import models

# class Department(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# from django.db import models

# class Employee(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=10)
#     company = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)

    def _str_(self):
        return self.name
    

class Login(models.Model):
    user_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    user_name = models.CharField(max_length=100)

    def _str_(self):
        return self.name    
    