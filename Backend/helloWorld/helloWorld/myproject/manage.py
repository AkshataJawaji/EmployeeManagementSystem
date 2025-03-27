# # 


# from django.db import models
# import uuid

# class Department(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Employee(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=10)
#     company = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     job_type = models.CharField(max_length=50)
#     date_of_joining = models.DateField()
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name



#!/usr/bin/env python
import os
import sys

import sys
sys.path.append('C:/Users/DELL/Desktop/helloWorld/myproject')


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
