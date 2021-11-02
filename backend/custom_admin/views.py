from app.cloudinary import upload_image
from app.models import Intern, Stack, User
from app.serializers import *
from django.contrib.auth.hashers import make_password
from django.http import Http404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from custom_admin.serializers import (
    AdminUserSerializer,
    ChangePasswordSerializer,
    InternAdminSerializer,
)


class CustomAuthToken(ObtainAuthToken):
    """[summary]

    Args:
        ObtainAuthToken ([type]): [description]
    """

    def post(self, request, *args, **kwargs):
        """[summary]

        Args:
            request ([type]): [description]

        Returns:
            [type]: [description]
        """
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


# ==================================================================================================================
class UserAdminCreateView(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]

    Returns:
        [type]: [description]
    """

    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, format=None):
        """[summary]

        Args:
            request ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        users = User.objects.all()
        serializer = AdminUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Returns:
            [type]: [description]
        """
        serializer = AdminUserSerializer(data=request.data)
        request.data["password"] = make_password("admin")
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
    """[summary]

    Args:
        APIView ([type]): [description]

    Raises:
        Http404: [description]

    Returns:
        [type]: [description]
    """

    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_object(self, user_id):
        """[summary]

        Args:
            user_id ([type]): [description]

        Raises:
            Http404: [description]

        Returns:
            [type]: [description]
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        """[summary]

        Args:
            request ([type]): [description]
            user_id ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        try:
            UserInfo = self.get_object(user_id)
            serializer = AdminUserSerializer(UserInfo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id, *args, **kwargs):
        """[summary]

        Args:
            request ([type]): [description]
            user_id ([type]): [description]

        Returns:
            [type]: [description]
        """
        user = self.get_object(user_id)
        serializer = AdminUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        """[summary]

        Args:
            request ([type]): [description]
            user_id ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """

        user_is_admin = request.user.is_admin

        if user_is_admin == False:
            return Response(
                {"mesage": "You can't perform this operation"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        UserInfo = self.get_object(user_id)
        UserInfo.delete()
        return Response(
            {"message": "User deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )


# ==================================================================================================================
class StackAdminCreateView(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]

    Returns:
        [type]: [description]
    """

    queryset = Stack.objects.all()
    serializer_class = StackSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, format=None):
        """[summary]

        Args:
            request ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        stacks = Stack.objects.all()
        serializer = StackSerializer(stacks, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """[summary]

        Args:
            request ([type]): [description]

        Returns:
            [type]: [description]
        """
        serializer = StackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ==================================================================================================================
class StackAdminUpdateView(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]

    Raises:
        Http404: [description]

    Returns:
        [type]: [description]
    """

    queryset = Stack.objects.all()
    serializer_class = StackSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_object(self, stack_id):
        """[summary]

        Args:
            stack_id ([type]): [description]

        Raises:
            Http404: [description]

        Returns:
            [type]: [description]
        """
        try:
            return Stack.objects.get(pk=stack_id)
        except Stack.DoesNotExist:
            raise Http404

    def get(self, request, stack_id, format=None):
        """[summary]

        Args:
            request ([type]): [description]
            stack_id ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        try:
            StackInfo = self.get_object(stack_id)
            serializer = StackSerializer(StackInfo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, stack_id, *args, **kwargs):
        """[summary]

        Args:
            request ([type]): [description]
            stack_id ([type]): [description]

        Returns:
            [type]: [description]
        """
        stack = self.get_object(stack_id)
        serializer = StackSerializer(stack, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, stack_id, format=None):
        """[summary]

        Args:
            request ([type]): [description]
            stack_id ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        user_is_admin = request.user.is_admin

        if user_is_admin == False:
            return Response(
                {"mesage": "You can't perform this operation"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        StackInfo = self.get_object(stack_id)
        StackInfo.delete()
        return Response(
            {"message": "Stack deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )


# ==================================================================================================================
class InternsAdminView(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]

    Returns:
        [type]: [description]
    """

    queryset = Intern.objects.all()
    serializer_class = InternAdminSerializer

    def get(self, request, format=None):
        """[summary]

        Args:
            request ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        interns = Intern.objects.all()
        serializer = InternAdminSerializer(interns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Returns:
            [type]: [description]
        """
        serializer = InternAdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ==================================================================================================================
class InternAdminUpdateView(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]

    Raises:
        Http404: [description]

    Returns:
        [type]: [description]
    """

    queryset = Intern.objects.all()
    serializer_class = InternSerializer

    def get_object(self, intern_id):
        """[summary]

        Args:
            intern_id ([type]): [description]

        Raises:
            Http404: [description]

        Returns:
            [type]: [description]
        """
        try:
            return Intern.objects.get(pk=intern_id)
        except Intern.DoesNotExist:
            raise Http404

    def get(self, request, intern_id, format=None):
        """[summary]

        Args:
            request ([type]): [description]
            intern_id ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        try:
            InternInfo = self.get_object(intern_id)
            serializer = InternSerializer(InternInfo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, intern_id, *args, **kwargs):
        """[summary]

        Args:
            request ([type]): [description]
            intern_id ([type]): [description]

        Returns:
            [type]: [description]
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
        """[summary]

        Args:
            request ([type]): [description]
            intern_id ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        user_is_admin = request.user.is_admin

        if user_is_admin == False:
            return Response(
                {"mesage": "You can't perform this operation"},
                status=status.HTTP_401_UNAUTHORIZED
            )
            
        StackInfo = self.get_object(intern_id)
        StackInfo.delete()
        return Response(
            {"message": "Intern deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )


class StaffInviteView(APIView):

    pass


class ChangePasswordView(UpdateAPIView):
    """[summary]

    Args:
        UpdateAPIView ([type]): [description]

    Returns:
        [type]: [description]
    """

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        """[summary]

        Args:
            queryset ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        """[summary]

        Args:
            request ([type]): [description]

        Returns:
            [type]: [description]
        """
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if serializer.data.get("password") != serializer.data.get("password2"):
                return Response(
                    {"password": "new password doesn't match "},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            self.object.set_password(serializer.data.get("password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
