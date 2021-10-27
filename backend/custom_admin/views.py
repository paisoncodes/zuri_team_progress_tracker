from django.db.models.query import QuerySet
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from custom_admin.serializers import (
    AdminUserSerializer,
    InternAdminSerializer,
)
from app.models import User, Stack, Intern, Jobs, NewsLetter
from app.serializers import *
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
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = AdminUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AdminUserSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data["permissions"] == "S":
                serializer.validated_data["staff"] = True
            if serializer.validated_data["permissions"] == "A":
                serializer.validated_data["staff"] = True
                serializer.validated_data["admin"] = True
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
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

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
        user = self.get_object(user_id)
        serializer = AdminUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        """
        Delete User
        """
        UserInfo = self.get_object(user_id)
        UserInfo.delete()
        return Response(
            {"message": "User deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )

# ==================================================================================================================
class StackAdminCreateView(APIView):
    """
    Create Stack View
    """

    queryset = Stack.objects.all()
    serializer_class = StackSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, format=None):
        stacks = Stack.objects.all()
        serializer = StackSerializer(stacks, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ==================================================================================================================
class StackAdminUpdateView(APIView):
    """
    Update Stack View
    """

    queryset = Stack.objects.all()
    serializer_class = StackSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_object(self, stack_id):
        try:
            return Stack.objects.get(pk=stack_id)
        except Stack.DoesNotExist:
            raise Http404

    def get(self, request, stack_id, format=None):
        """
        Get Stack Details
        """
        try:
            StackInfo = self.get_object(stack_id)
            serializer = StackSerializer(StackInfo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, stack_id, *args, **kwargs):
        stack = self.get_object(stack_id)
        serializer = StackSerializer(stack, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, stack_id, format=None):
        """
        Delete Stack
        """
        StackInfo = self.get_object(stack_id)
        StackInfo.delete()
        return Response(
            {"message": "Stack deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
# ==================================================================================================================
class InternsAdminView(APIView):
    queryset = Intern.objects.all()
    serializer_class = InternAdminSerializer
    def get(self, request, format=None):
        interns = Intern.objects.all()
        serializer = InternAdminSerializer(interns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = InternAdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ==================================================================================================================
class InternAdminUpdateView(APIView):
    """
    Update Stack View
    """

    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_object(self, intern_id):
        try:
            return Intern.objects.get(pk=intern_id)
        except Intern.DoesNotExist:
            raise Http404

    def get(self, request, intern_id, format=None):
        """
        Get Stack Details
        """
        try:
            InternInfo = self.get_object(intern_id)
            serializer = InternSerializer(InternInfo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, intern_id, *args, **kwargs):
        """
        Updates an intern
        """
        try:
            instance = Intern.objects.get(pk=intern_id)
            if request.data.get("is_employed"):
                is_employed = request.data.get("is_employed")
            else:
                is_employed = False
            
            if request.data.get("username"):
                username = request.data.get("username")
            else:
                username = instance.username

            if request.data.get("stack"):
                stack = request.data.get("stack")
            else:
                stack = instance.stack

            if request.data.get("gender"):
                gender = request.data.get("gender")
            else:
                gender = instance.gender

            if request.data.get("state"):
                state = request.data.get("state")
            else:
                state = instance.state

            if request.data.get("batch"):
                batch = request.data.get("batch")
            else:
                batch = instance.batch

            if request.FILES:
                image = request.FILES["image"]
                data = {
                    "username": username,
                    "full_name": request.data.get("full_name"),
                    "stack": stack,
                    "gender": gender,
                    "about": request.data.get("about"),
                    "state": state,
                    "batch": batch,
                    "is_employed": is_employed,
                    "current_salary": request.data.get("current_salary"),
                    "picture": upload_image(image),
                }
                instance.save()

                serializer = InternSerializer(instance, data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                data = {
                    "username": username,
                    "full_name": request.data.get("full_name"),
                    "stack": stack,
                    "gender": gender,
                    "about": request.data.get("about"),
                    "state": state,
                    "batch": batch,
                    "is_employed": is_employed,
                    "current_salary": request.data.get("current_salary"),
                    "picture": instance.picture,
                }
                instance.save()

                serializer = InternSerializer(instance, data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"exception": f"{e}"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, intern_id, format=None):
        """
        Delete Stack
        """
        StackInfo = self.get_object(intern_id)
        StackInfo.delete()
        return Response(
            {"message": "Intern deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )

class StaffInviteView(APIView):

    pass