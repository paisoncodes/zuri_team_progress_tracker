from rest_framework import serializers, status, views
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

# Create your views here.


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

