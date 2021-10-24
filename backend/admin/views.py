from django.db.models.query import QuerySet
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from admin.serializers import (
    AdminUserSerializer,
)
from app.models import User, Intern, Jobs, NewsLetter
from .serializers import *
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, JSONParser
from app.cloudinary import upload_image

# Create your views here.

# ==================================================================================================================
class UserAdminCreateView(APIView):
    """
    Create Users View
    """

    queryset = User.objects.all()
    serializer_class = AdminUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = AdminUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ==================================================================================================================
class UserAdminUpdateView(APIView):
    """
    Update Users View
    """

    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]

    def get_object(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        """
        Get User Details
        """
        try:
            UserInfo = self.get_object(user_id)
            serializer = AdminUserSerializer(UserInfo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id, *args, **kwargs):
        user = User.objects.get(pk=user_id)
        serializer = AdminUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        """
        Delete User
        """
        UserInfo = User.objects.get(pk=user_id)
        UserInfo.delete()
        return Response(
            {"message": "User deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )

# ==================================================================================================================
