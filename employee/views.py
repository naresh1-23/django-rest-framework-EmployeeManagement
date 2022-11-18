from django.shortcuts import render
from .models import Employee
from rest_framework import generics
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from rest_framework import viewsets

class EmployeeList(generics.ListCreateAPIView):
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class Employeeviewset(viewsets.ModelViewSet):
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
       


# Create your views here.
