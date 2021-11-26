import csv
import os
from django.http.response import Http404
from .models import Intern, Stack, Statistic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent

# link = os.path.join(BASE_DIR, "app/zuri.csv")
# print(link)
YEAR = 2021

csvFilePath = "app/zuri.csv"

main_data = []

id = 1
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        rows["Psami_id"] = id
        main_data.append(rows)
        id += 1


def get_available_stacks(main_data):
    stacks = []
    for data in main_data:
        stacks.append(data["Your Stacks"])

    only_stack = []

    for stack in stacks:
        stack_list = stack.split(",")
        for item in stack_list:
            if item not in only_stack and item != "":
                only_stack.append(item)

    return only_stack


@api_view(["POST"])
def create_stacks(request):
    try:
        stacks = get_available_stacks(main_data)
        for stack in stacks:
            instance = Stack.objects.create(name=stack, batch=YEAR)
            instance.save()
        return Response({"message": "Stacks Populated"})
    except Exception as e:
        return Response(
            {"message": f"see your Big head: {e}"}, status=status.HTTP_400_BAD_REQUEST
        )


def get_stats(main_data):
    male = 0
    female = 0
    idict = {}
    for data in main_data:
        if data["Gender"] == "Male":
            male += 1
        elif data["Gender"] == "Female":
            female += 1
    finalist = male + female

    idict["Male"] = male
    idict["Female"] = female
    idict["Finalist"] = finalist

    return idict


@api_view(["POST"])
def create_stat(request):
    try:
        stat = get_stats(main_data)
        instance = Statistic.objects.create(
            male=stat["Male"],
            female=stat["Female"],
            year=YEAR,
            finalist=stat["Finalist"],
        )

        instance.save()
        return Response({"message": "Statistic Populated"})
    except Exception as e:
        return Response(
            {"message": f"see your Big head: {e}"}, status=status.HTTP_400_BAD_REQUEST
        )


def get_image_link(photo):
    x = photo.index("(")
    y = photo.index(")")
    image = photo[x + 1 : y]
    if image[0:4] == "http":
        return image
    else:
        return "https://res.cloudinary.com/psami-wondah/image/upload/v1635282292/profile_pic_yxkand.png"


def create_intern(data):
    if data["Gender"] == "Male":
        gender = "M"
    elif data["Gender"] == "Female":
        gender = "F"
    elif data["Gender"] == "":
        return

    if data["If you have a job, how much do you earn?"] != "":
        employed = True
    else:
        employed = False

    intern = Intern.objects.create(
        full_name=data["Name"],
        gender=gender,
        email=data["Email address"],
        about="about me",
        state=data["The State you Live in"],
        batch=YEAR,
        is_employed=employed,
        current_salary=2500,
        picture="https://res.cloudinary.com/psami-wondah/image/upload/v1635282292/profile_pic_yxkand.png"
    )
    intern.save()
    stack_data_list = data["Your Stacks"].split(",")
    if "" not in stack_data_list:
        for item in stack_data_list:
            instance = Stack.objects.get(name=item, batch=YEAR)
            intern.stack.add(instance)


@api_view(["POST"])
def create_an_intern(request):
    try:

        for data in main_data:
            try:
                create_intern(data)
            except Exception:
                pass

        return Response({"message": "beast"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": f"ode {e}"}, status=status.HTTP_400_BAD_REQUEST)


# stack = models.ManyToManyField(Stack, related_name="intern_stack", blank=True)
