from django.shortcuts import render,redirect,get_list_or_404
from .models import*
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Studentserializer

# Create your views here.
class Studentlist(APIView):

    def get(self,request):
        a=Student.objects.all()
        s=Studentserializer(a,many=True)
        return Response(s.data)

    def post(self):
        pass    

