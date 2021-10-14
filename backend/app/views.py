from rest_framework import serializers, status, views
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, UpdateUserSerializer

# Create your views here.
class UserCreateView(APIView):
    '''
    Create Users View
    '''
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
        

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class UserUpdateView(APIView):
    '''
    Update Users View
    '''
    serializer_class = UpdateUserSerializer

    def put(self, request, user_id,  *args, **kwargs):
        user = User.objects.get(pk=user_id)
        serializer = UpdateUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
  


class UserClassView(APIView):

    def get(self, request, pk, format=None):
        '''
        Get User Details
        '''
        UserInfo = self.get_object(pk)        
        serializer = UserSerializer(UserInfo)
        if UserInfo:
            UserInfo.get()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"message": "Unable to retrieve user details"},
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        '''
        Delete Users
        '''
        UserInfo = self.get_object(pk)
        UserInfo.delete()
        return Response(
        {"message": "User deleted successfully."},
        status=status.HTTP_204_NO_CONTENT,
        )

