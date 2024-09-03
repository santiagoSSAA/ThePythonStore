from typing import Union

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, UserUpdateSerializer

# Create your views here.
class UserListCreate(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(APIView):
    def get_object(self, pk) -> Union[User, Response]:
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"detail": "user not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        response = self.get_object(pk)
        if isinstance(response, Response):
            return Response
        serializer = UserSerializer(response)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        response = self.get_object(pk)
        if isinstance(response, Response):
            return Response
        serializer = UserUpdateSerializer(response, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        