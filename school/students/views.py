from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Student
from .serializer import StudentSerializer

# GET all & POST
class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# GET single student
class StudentDetail(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer