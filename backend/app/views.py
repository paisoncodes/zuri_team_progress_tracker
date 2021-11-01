from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .cloudinary import upload_image
from .models import Intern, Jobs, NewsLetter, Stack
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, JSONParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics

# Create your views here.

paginator = PageNumberPagination()
paginator.page_size = 20
# ==================================================================================================================


def convert_stack_to_list(data):
    """[summary]

    Args:
        data ([type]): [description]
    """
    stacks = []
    for item in data["stack"]:
        stacks.append(item["name"])
    data["stack"] = stacks
# ==================================================================================================================


class JobView(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]

    Returns:
        [type]: [description]
    """
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer

    def post(self, request, intern_id):
        """[summary]

        Args:
            request ([type]): [description]
            intern_id ([type]): [description]

        Returns:
            [type]: [description]
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
        """[summary]

        Args:
            request ([type]): [description]
            intern_id ([type]): [description]

        Returns:
            [type]: [description]
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
    """[summary]

    Args:
        UpdateAPIView ([type]): [description]

    Returns:
        [type]: [description]
    """
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.AllowAny,)

    def put(self, request, intern_id, job_id):
        """[summary]

        Args:
            request ([type]): [description]
            intern_id ([type]): [description]
            job_id ([type]): [description]

        Returns:
            [type]: [description]
        """
        intern = Intern.objects.get(pk=intern_id)
        instance = Jobs.objects.get(intern=intern, pk=job_id)
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
        """[summary]

        Args:
            request ([type]): [description]
            intern_id ([type]): [description]
            pk ([type]): [description]

        Returns:
            [type]: [description]
        """
        intern = Intern.objects.get(pk=intern_id)
        job = Jobs.objects.get(pk=pk, intern=intern)
        serializer = JobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)
# ==================================================================================================================


class InternDetailView(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]
    """

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
        intern = self.get_object(intern_id)
        serializer = InternSerializer(intern)
        data = serializer.data
        convert_stack_to_list(data)

        return Response(data)

    def delete(self, request, intern_id, format=None):
        """[summary]

        Args:
            request ([type]): [description]
            intern_id ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        intern = self.get_object(intern_id)
        intern.delete()
        return Response(status=status.HTTP_200_OK)
# ==================================================================================================================


class InternsView(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]
    """

    def get(self, request, format=None):
        """[summary]

        Args:
            request ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        interns = Intern.objects.all()
        serializer = InternSerializer(interns, many=True)
        data = serializer.data
        for datum in data:
            convert_stack_to_list(datum)
        paginated_data = paginator.paginate_queryset(data, request=request)
        return paginator.get_paginated_response(paginated_data)

    def post(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Returns:
            [type]: [description]
        """

        serializer = InternSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ==================================================================================================================


class InternUpdate(UpdateAPIView):
    """[summary]

    Args:
        UpdateAPIView ([type]): [description]

    Returns:
        [type]: [description]
    """
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    permission_classes = (permissions.AllowAny,)

    def put(self, request, intern_id):
        """[summary]

        Args:
            request ([type]): [description]
            intern_id ([type]): [description]

        Returns:
            [type]: [description]
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
        """[summary]

        Args:
            request ([type]): [description]
            intern_id ([type]): [description]

        Returns:
            [type]: [description]
        """
        intern = Intern.objects.get(pk=intern_id)
        serializer = InternSerializer(intern)
        data = serializer.data
        convert_stack_to_list(data)
        return Response(data)

    def patch(self, request, intern_id):
        """[summary]

        Args:
            request ([type]): [description]
            intern_id ([type]): [description]

        Returns:
            [type]: [description]
        """
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


class Search(generics.ListAPIView):

    """[summary]

    Args:
        generics ([type]): [description]
    """
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    filterset_fields = ['id', 'full_name', 'stack']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['id', 'full_name', 'stack']
    ordering = ('full_name',)
    search_fields = ['id', 'full_name', 'stack__name']

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        for datum in data:
            convert_stack_to_list(datum)
        paginated_data = paginator.paginate_queryset(data, request=request)
        return paginator.get_paginated_response(paginated_data)

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     data = serializer.data
        #     for datum in data:
        #         convert_stack_to_list(datum)
        #     return self.get_paginated_response(data)

        # serializer = self.get_serializer(queryset, many=True)
        # data = serializer.data
        # for datum in data:
        #     convert_stack_to_list(datum)
        # return Response(data)


# ================================================================================================================
class NewsLetterSubscribeView(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]

    Returns:
        [type]: [description]
    """
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer

    def post(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Returns:
            [type]: [description]
        """
        serializer = NewsLetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ==================================================================================================================


class NewsLetterSubscribersView(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]

    Returns:
        [type]: [description]
    """

    def get(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        subscriber = NewsLetter.objects.all()
        serializer = NewsLetterSerializer(subscriber, many=True)
        return Response(serializer.data)
# ==================================================================================================================


class InternStackList(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]
    """

    def get(self, request, stack):
        """[summary]

        Args:
            request ([type]): [description]
            stack ([type]): [description]

        Returns:
            [type]: [description]
        """
        instance = Stack.objects.get(name=stack)
        interns = Intern.objects.filter(stack=instance)
        serializer = InternSerializer(interns, many=True)
        data = serializer.data
        for datum in data:
            convert_stack_to_list(datum)
        paginated_data = paginator.paginate_queryset(data, request=request)
        return paginator.get_paginated_response(paginated_data)
# ==================================================================================================================


class StatisticView(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]
    """

    def get(self, request, batch, format=None):
        """[summary]

        Args:
            request ([type]): [description]
            batch ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        try:
            statistic = Statistic.objects.get(year=batch)
            # serializer = StatisticSerializer(statistic)
            # data = serializer.data
            all_interns = Intern.objects.filter(batch=batch)
            employed_interns = Intern.objects.filter(
                batch=batch, is_employed=True)
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
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = []
    try:
        statistics = Statistic.objects.all()
        for stat in statistics:
            all_interns = Intern.objects.filter(batch=stat.year)
            employed_interns = Intern.objects.filter(
                batch=stat.year, is_employed=True)

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
    """[summary]

    Args:
        request ([type]): [description]
        batch ([type]): [description]

    Returns:
        [type]: [description]
    """
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
    """[summary]

    Args:
        APIView ([type]): [description]
    """

    def get(self, request, batch):
        """[summary]

        Args:
            request ([type]): [description]
            batch ([type]): [description]

        Returns:
            [type]: [description]
        """
        try:
            interns = Intern.objects.filter(batch=batch)
            serializer = InternSerializer(interns, many=True)
            data = serializer.data
            for datum in data:
                convert_stack_to_list(datum)
            paginated_data = paginator.paginate_queryset(data, request=request)
            return paginator.get_paginated_response(paginated_data)
        except Exception as e:
            return Response({"Wahala": f"{e}"}, status.HTTP_400_BAD_REQUEST)
# ==================================================================================================================


@api_view(["GET"])
def get_interns_by_year_and_stack(request, batch, stack):
    """[summary]

    Args:
        request ([type]): [description]
        batch ([type]): [description]
        stack ([type]): [description]

    Returns:
        [type]: [description]
    """
    try:
        instance = Stack.objects.get(name=stack, batch=batch)
        interns = Intern.objects.filter(stack=instance)
        serializer = InternSerializer(interns, many=True)
        data = serializer.data
        for datum in data:
            convert_stack_to_list(datum)
        paginated_data = paginator.paginate_queryset(data, request=request)
        return paginator.get_paginated_response(paginated_data)
    except Exception as e:
        return Response({"Wahala": f"{e}"}, status.HTTP_400_BAD_REQUEST)
# ==================================================================================================================


class GetStacksPerBatch(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]
    """

    def get(self, request, batch):
        """[summary]

        Args:
            request ([type]): [description]
            batch ([type]): [description]

        Returns:
            [type]: [description]
        """
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
# ==================================================================================================================


class SponsorView(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]

    Returns:
        [type]: [description]
    """
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )
    queryset = None

    def post(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Returns:
            [type]: [description]
        """
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
        """[summary]

        Args:
            request ([type]): [description]

        Returns:
            [type]: [description]
        """
        sponsor_queryset = Sponsor.objects.all()
        serializer = SponsorSerializer(sponsor_queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, id):
        """[summary]

        Args:
            request ([type]): [description]
            id ([type]): [description]

        Returns:
            [type]: [description]
        """
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
# ==================================================================================================================


@api_view(["GET"])
def get_all_jobs(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    instance = Jobs.objects.all()
    interns = []
    for job in instance:
        serializer = InternSerializer(job.intern)
        data = serializer.data
        interns.append(data)
    return Response({"data": interns})

# class DynamicSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         return request.GET.getlist('search_fields', [])
