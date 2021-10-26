from os import name
from django.db.models.query import QuerySet
from rest_framework import status, permissions
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .serializers import (
    UserSerializer,
    UserUpdateSerializer,
    JobSerializer,
    InternUpdateSerializer,
)
from .models import User, Intern, Jobs, NewsLetter, Stack
from .serializers import *
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, JSONParser
from .cloudinary import upload_image

# Create your views here.


def convert_stack_to_list(data):
    stacks = []
    for item in data["stack"]:
        stacks.append(item["name"])

    data["stack"] = stacks


# ==================================================================================================================
class UserCreateView(APIView):
    """
    Create Users View
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ==================================================================================================================


class UserUpdateView(APIView):
    """
    Update Users View
    """

    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

    def put(self, request, user_id, *args, **kwargs):
        user = User.objects.get(pk=user_id)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ==================================================================================================================


class UserDetailView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer()

    def get(self, request, user_id):
        """
        Get User Details
        """
        try:
            UserInfo = User.objects.get(pk=user_id)
            serializer = UserSerializer(UserInfo, data=request.data)
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


# ==================================================================================================================


class JobView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer

    def post(self, request, intern_id):
        """
        Creates a new job for a particular intern
        """
        try:
            intern = Intern.objects.get(pk=intern_id)
            image = request.FILES["image"]

            serializer = JobSerializer(data=request.data)
            if serializer.is_valid():
                serializer.validated_data["intern"] = intern
                serializer.validated_data["job_logo"] = upload_image(image)
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        except Exception as e:
            return Response({"exception": f"{e}"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, intern_id):
        """
        Retrieves and list the job details of an intern
        """
        try:
            intern = Intern.objects.get(pk=intern_id)
            jobsList_objects = Jobs.objects.filter(intern=intern)
            if len(jobsList_objects) > 0:
                serializer = JobSerializer(jobsList_objects, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response("Unemployed", status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"exception": f"{e}"}, status=status.HTTP_404_NOT_FOUND)


# ==================================================================================================================


class JobUpdateView(UpdateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.AllowAny,)

    def put(self, request, intern_id, pk):
        """
        Updates a job model
        """
        intern = Intern.objects.get(pk=intern_id)
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

    def get(self, request, intern_id, pk):
        """
        Gets a particular job detail
        """
        intern = Intern.objects.get(pk=intern_id)
        job = Jobs.objects.get(pk=pk, intern=intern)
        serializer = JobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ==================================================================================================================


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
        data = serializer.data
        convert_stack_to_list(data)

        return Response(data)

    def delete(self, request, pk, format=None):
        intern = self.get_object(pk)
        intern.delete()
        return Response(status=status.HTTP_200_OK)


# ==================================================================================================================


class InternsView(APIView):
    """
    endpoint to create an intern or get a list of interns
    create:
        request body:
            {
            "username": "user",
            "full_name": "fullname",
            "stack": "Backend",
            "state": "Oyo",
            "gender": "M",
            "about": "Random text",
            "batch": "2020",
            "current_salary": "3000",
            "is_employed": "True",
            "picture": "https://ocdn.eu/pulscms-transforms/1/9zVk9kuTURBXy84MTcxYmNmNy0zMmIwLTQ1MzAtOTE0MS1iMWU1Y2Y1MTNjN2MuanBlZ5GTBc0DFs0BroGhMAU"
            }
    """

    queryset = Intern.objects.all()
    serializer_class = InternSerializer

    def get(self, request, format=None):
        interns = Intern.objects.all()
        serializer = InternSerializer(interns, many=True)
        data = serializer.data
        for datum in data:
            convert_stack_to_list(datum)
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = InternSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ==================================================================================================================


class InternUpdateView(APIView):
    """
    endpoint to create or update an intern
    create:
        request body:
            {
            "username": "user",
            "full_name": "fullname",
            "stack": "Backend",
            "state": "Oyo",
            "gender": "M",
            "about": "Random text",
            "batch": "2020",
            "current_salary": "3000",
            "is_employed": "True",
            "picture": "https://ocdn.eu/pulscms-transforms/1/9zVk9kuTURBXy84MTcxYmNmNy0zMmIwLTQ1MzAtOTE0MS1iMWU1Y2Y1MTNjN2MuanBlZ5GTBc0DFs0BroGhMAU"
            }

     update:
        request_body:
            {   "intern_id":1,
                "data":
                    {"username": "user",
                    "full_name": "fullname",
                    "stack": "Backend",
                    "state": "Oyo",
                    "gender": "M",
                    "about": "Random text",
                    "batch": "2020",
                    "current_salary": "3000",
                    "is_employed": "True",
                    "picture": "https://ocdn.eu/pulscms-transforms/1/9zVk9kuTURBXy84MTcxYmNmNy0zMmIwLTQ1MzAtOTE0MS1iMWU1Y2Y1MTNjN2MuanBlZ5GTBc0DFs0BroGhMAU"
                    }}
    """

    def put(self, request):
        intern_id = request.data.pop("intern_id")
        try:
            intern = Intern.objects.get(pk=intern_id)
        except Intern.DoesNotExist:
            return Response(
                {"message": "This intern does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = InternSerializer(intern, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ==================================================================================================================


class InternUpdate(UpdateAPIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    permission_classes = (permissions.AllowAny,)

    def put(self, request, intern_id):
        """
        Updates an intern
        """
        try:
            if request.FILES:
                image = request.FILES["image"]
                instance = Intern.objects.get(pk=intern_id)
                if request.data.get("is_employed"):
                    is_employed = request.data.get("is_employed")
                else:
                    is_employed = False
                data = {
                    "full_name": request.data.get("full_name"),
                    "stack": instance.stack,
                    "gender": instance.gender,
                    "about": request.data.get("about"),
                    "state": instance.state,
                    "batch": instance.batch,
                    "is_employed": is_employed,
                    "current_salary": request.data.get("current_salary"),
                    "picture": upload_image(image),
                }
                instance.save()

                serializer = InternSerializer(instance, data=data)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)

                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                instance = Intern.objects.get(pk=intern_id)
                if request.data.get("is_employed"):
                    is_employed = request.data.get("is_employed")
                else:
                    is_employed = False
                data = {
                    "full_name": request.data.get("full_name"),
                    "stack": instance.stack,
                    "gender": instance.gender,
                    "about": request.data.get("about"),
                    "state": instance.state,
                    "batch": instance.batch,
                    "is_employed": is_employed,
                    "current_salary": request.data.get("current_salary"),
                    "picture": instance.picture,
                }
                instance.save()

                serializer = InternSerializer(instance, data=data)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)

                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"exception": f"{e}"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, intern_id):
        intern = Intern.objects.get(pk=intern_id)
        serializer = InternSerializer(intern)
        data = serializer.data
        convert_stack_to_list(data)
        return Response(data)

    def patch(self, request, intern_id):
        image = request.FILES["image"]
        try:
            instance = Intern.objects.get(pk=intern_id)
        except Intern.DoesNotExist:
            data = {"error": "no user with such id"}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        instance.picture = upload_image(image)
        instance.save()
        serializer = InternSerializer(instance)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


# ==================================================================================================================


class NewsLetterSubscribeView(APIView):
    """
    Creates Subscribers For NewsLetters
    """

    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer

    def post(self, request, *args, **kwargs):
        serializer = NewsLetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ==================================================================================================================


class NewsLetterSubscribersView(APIView):
    """
    Lists all the NewsLetter Subscribers
    """

    def get(self, request, *args, **kwargs):
        subscriber = NewsLetter.objects.all()
        serializer = NewsLetterSerializer(subscriber, many=True)
        return Response(serializer.data)


class InternStackList(APIView):
    def get(self, request, stack):
        instance = Stack.objects.get(name=stack)
        interns = Intern.objects.filter(stack=instance)
        serializer = InternSerializer(interns, many=True)
        data = serializer.data
        for datum in data:
            convert_stack_to_list(datum)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ==================================================================================================================


class StatisticView(APIView):
    """
    Intern Statistics
    """

    def get(self, request, batch, format=None):
        try:
            statistic = Statistic.objects.get(year=batch)
            # serializer = StatisticSerializer(statistic)
            # data = serializer.data
            all_interns = Intern.objects.filter(batch=batch)
            employed_interns = Intern.objects.filter(batch=batch, is_employed=True)
            # print(data)
            response_body = {
                "year": statistic.year,
                "male": statistic.male,
                "female": statistic.female,
                "participants": statistic.participant,
                "finalists": len(all_interns),
                "employed_finalists": len(employed_interns),
            }

            return Response(response_body, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"exception": f"{e}"}, status=status.HTTP_404_NOT_FOUND)


# ==================================================================================================================


@api_view(["GET"])
def all_stats(request):
    data = []

    try:
        statistics = Statistic.objects.all()
        for stat in statistics:
            all_interns = Intern.objects.filter(batch=stat.year)
            employed_interns = Intern.objects.filter(batch=stat.year, is_employed=True)

            response_body = {
                "year": stat.year,
                "male": stat.male,
                "female": stat.female,
                "participants": stat.participant,
                "finalists": len(all_interns),
                "employed_finalists": len(employed_interns),
            }

            data.append(response_body)
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"exception": f"{e}"}, status=status.HTTP_404_NOT_FOUND)


# ==================================================================================================================


@api_view(["GET"])
def total_salary(request, batch):
    interns = Intern.objects.filter(batch=batch, is_employed=True)
    salary = 0
    try:
        for intern in interns:
            salary = salary + intern.current_salary
        return Response({"total_salary": f"{salary}"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"Wahala": f"{e}"}, status.HTTP_400_BAD_REQUEST)


# ==================================================================================================================


class BatchList(APIView):
    def get(self, request, batch):
        try:
            interns = Intern.objects.filter(batch=batch)
            serializer = InternSerializer(interns, many=True)
            data = serializer.data
            for datum in data:
                convert_stack_to_list(datum)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Wahala": f"{e}"}, status.HTTP_400_BAD_REQUEST)


# ==================================================================================================================


@api_view(["get"])
def get_interns_by_year_and_stack(request, batch, stack):
    try:
        instance = Stack.objects.get(name=stack, batch=batch)
        interns = Intern.objects.filter(stack=instance)
        serializer = InternSerializer(interns, many=True)
        data = serializer.data
        for datum in data:
            convert_stack_to_list(datum)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"Wahala": f"{e}"}, status.HTTP_400_BAD_REQUEST)


# ==================================================================================================================


class GetStacksPerBatch(APIView):
    def get(self, request, batch):
        try:
            stack_detail = {}
            stacks = []
            year = Stack.objects.filter(batch=batch)
            for leap_year in year:
                stack_detail[leap_year.name] = len(
                    Intern.objects.filter(stack=leap_year)
                )
            for stack in year:
                stacks.append(stack.name)
            data = {"stacks": stacks, "stack_data": stack_detail}
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Message": f"{e}"}, status.HTTP_400_BAD_REQUEST)


class SponsorView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )
    queryset = None

    def post(self, request):
        serializer = SponsorSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        image = request.FILES["logo"]

        Sponsor.objects.create(
            name=serializer.validated_data.get("name"), logo=upload_image(image)
        )

        data = {
            "status": status.HTTP_201_CREATED,
            "message": "Sponsor created",
            "error": False,
        }

        return Response(data, status=status.HTTP_201_CREATED)

    def get(self, request):
        sponsor_queryset = Sponsor.objects.all()
        serializer = SponsorSerializer(sponsor_queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, id):
        try:
            sponsor = Sponsor.objects.get(id=id)
            sponsor.delete()
            data = {
                "status": status.HTTP_200_OK,
                "message": "Sponsor deleted",
                "error": False,
            }
            return Response(data, status.HTTP_200_OK)
        except Sponsor.DoesNotExist:
            data = {
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Sponsor not found",
                "error": True,
            }
            return Response(data, status.HTTP_404_NOT_FOUND)

        except:
            data = {
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "something went wrong",
                "error": True,
            }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def get_all_jobs(request):
    instance = Jobs.objects.all()
    interns = []
    for job in instance:
        serializer = InternSerializer(job.intern)
        data = serializer.data
        interns.append(data)
    return Response({"data": interns})
