from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from django.shortcuts import render

# Create your views here.



class HelloApiView(APIView):
    """Test APIView"""
    serializer_class = serializers.HelloSerializer


    def get(self, requiest, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs',
        ]

        return Response ({'message' : 'Hello', 'an_apiview': an_apiview, })


    def post(self, requiest):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=requiest.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )


    def put(self, requiest, pk=None):
        """Handle updating an Object"""
        return Response({'method': 'PUT'})

    def patch(self, requiest, pk=None):
        """Handlea partial update of an object"""
        return Response ({'method' : 'PATCH'})


    def delete(self, requiest, pk=None):
        """Delete an object"""
        return Response ({'method' : 'DELETE'})
