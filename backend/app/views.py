from rest_framework import  status, views
from rest_framework.views import APIView
# from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .serializers import UserSerializer, UserUpdateSerializer, JobSerializer
from .models import User,Intern
from .serializers import *
from django.http import Http404

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
    serializer_class = UserUpdateSerializer

    def put(self, request, user_id,  *args, **kwargs):
        user = User.objects.get(pk=user_id)
        serializer = UserUpdateSerializer(user, data=request.data)
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

class JobView(APIView):
    def post(self, request, username):
        intern = Intern.objects.get(username=username)
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["intern"]=intern
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)



        

######### Intern Models
class InternDetailView(APIView):
    """
        Intern Update View
    """

    def get_object(self, pk):
        try:
            return Intern.objects.get(pk=pk)
        except Intern.DoesNotExist:
            raise Http404


    def delete(self, request, pk, format=None):
        intern = self.get_object(pk)
        intern.delete()
        
        return Response(status=status.HTTP_200_OK)
