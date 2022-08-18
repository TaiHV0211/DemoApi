'''
----------------NOTTTTT UNDERSTAND----------------------------
'''

# from rest_framrwork import serializers
from dataclasses import fields
from rest_framework import serializers
from EmployeeApi.models import Departments,Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')

