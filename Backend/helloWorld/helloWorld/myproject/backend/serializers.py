from rest_framework import serializers
from .models import Employee
from .models import Login

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '_all_'




class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '_all_'