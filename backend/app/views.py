from django.db.models.query import QuerySet
from rest_framework import status, views, permissions
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .serializers import UserSerializer, UserUpdateSerializer, JobSerializer
from .models import User, Intern, Jobs, NewsLetter
from .serializers import *
from django.http import Http404
from django.core import serializers
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class UserCreateView(APIView):
    """
    Create Users View
    """

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
    """
    Update Users View
    """

    serializer_class = UserUpdateSerializer

    def put(self, request, user_id, *args, **kwargs):
        user = User.objects.get(pk=user_id)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get(self, request, user_id):
        """
        Get User Details
        """
        try:
            UserInfo = User.objects.get(pk=user_id)
            serializer = UserUpdateSerializer(UserInfo, data=request.data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"message": "Unable to retrieve user details"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

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


class JobView(APIView):
    def post(self, request, username):
        """
        Creates a new job for a particular intern
        """
        try:
            intern = Intern.objects.get(username=username)

            serializer = JobSerializer(data=request.data)
            if serializer.is_valid():
                serializer.validated_data["intern"] = intern
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        except Exception as e:
            return Response({"exception": f"{e}"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, username):
        """
        Retrieves and list the job details of an intern
        """
        try:
            intern = Intern.objects.get(username=username)
            jobsList_objects = Jobs.objects.filter(intern=intern)
            if len(jobsList_objects) > 0:
                serializer = JobSerializer(jobsList_objects, many=True)
                print(serializer.data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response("Unemployed", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"exception": f"{e}"}, status=status.HTTP_404_NOT_FOUND)


class JobUpdateView(UpdateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.AllowAny,)

    def put(self, request, username, pk):
        """
        Updates a job model
        """
        intern = Intern.objects.get(username=username)
        instance = Jobs.objects.get(intern=intern, pk=pk)
        data = {
            "job_title": request.data.get("job_title"),
            "company_name": request.data.get("company_name"),
            "gotten_at": request.data.get("gotten_at"),
            "last_updated_at": request.data.get("last_updated_at"),
            "job_description": request.data.get("job_description"),
            "currently_active": request.data.get("currently_active"),
        }
        instance.save()

        serializer = JobSerializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def get(self, request, username, pk):
        """
        Gets a particular job detail
        """
        intern = Intern.objects.get(username=username)
        job = Jobs.objects.get(pk=pk, intern=intern)
        serializer = JobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)


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

    def get(self, request, pk, format=None):
        intern = self.get_object(pk)
        serializer = InternSerializer(intern)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        intern = self.get_object(pk)
        intern.delete()
        return Response(status=status.HTTP_200_OK)


class InternList(APIView):
    def get(self, request, format=None):
        interns = Intern.objects.all()
        serializer = InternSerializer(interns, many=True)
        return Response(serializer.data)


class InternCreateUpdateView(APIView):
    def post(self, request):
        serializer = InternSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request):
        intern_id = request.data.pop("intern_id")
        try:
            intern = Intern.objects.get(pk=intern_id)
        except Intern.DoesNotExist:
            return Response(
                {"message": "This intern does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = InternSerializer(data=request, instance=intern)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NewsLetterSubscribeView(APIView):
    """
    Creates Subscribers For NewsLetters
    """

    serializer_class = NewsLetterSerializer

    def post(self, request, *args, **kwargs):
        serializer = NewsLetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsLetterSubscribersView(APIView):
    """
    Lists all the NewsLetter Subscribers
    """

    serializer_class = NewsLetterSerializer

    def get(self, request, *args, **kwargs):
        subscriber = NewsLetter.objects.all()
        serializer = NewsLetterSerializer(subscriber, many=True)
        return Response(serializer.data)


# {
# "subscriber_email" : "noor@gmail.com"
# }


class InternStackList(APIView):
    def get(self, request, stack):
        interns = Intern.objects.filter(stack=stack)
        serializer = InternSerializer(interns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StatisticView(APIView):
    """
    Intern Statistics
    """
    def get(self, request, format=None):
        queryset = Statistic.objects.all()
        serializer = StatisticSerializer(queryset, many=True)
        return Response(serializer.data)