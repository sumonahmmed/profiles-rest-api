from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.



class HelloApiView(APIView):
    """Test APIView"""


    def get(self, requiest, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs',
        ]

        return Response ({'message' : 'Hello', 'an_apiview': an_apiview, })
