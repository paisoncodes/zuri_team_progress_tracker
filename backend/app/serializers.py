from rest_framework import serializers

from .models import *


# ==================================================================================================================
class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ["name"]
# ==================================================================================================================
class InternSerializer(serializers.ModelSerializer):
    stack = StackSerializer(many=True, read_only=True)

    class Meta:
        model = Intern
        fields = [
            "id",
            "full_name",
            "stack",
            "state",
            "gender",
            "about",
            "batch",
            "current_salary",
            "is_employed",
            "picture",
        ]
# ==================================================================================================================
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = [
            "id",
            "job_title",
            "company_name",
            "gotten_at",
            "job_description",
            "currently_active",
            "job_logo",
        ]
# ==================================================================================================================
class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = "__all__"
# ==================================================================================================================
class InternUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = "__all__"
# ==================================================================================================================
class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = "__all__"
# ==================================================================================================================
class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = "__all__"
