from django.db import models
from rest_framework import serializers

from .models import *




# ==================================================================================================================

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=200)
    # password = serializers.PasswordField(max_length=100)
    address = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.address = validated_data.get("address", instance.address)
        instance.city = validated_data.get("city", instance.city)
        instance.state = validated_data.get("state", instance.state)

        instance.save()
        return instance


# ==================================================================================================================

class UserUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    first_name = serializers.CharField(max_length=100, required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(max_length=200, required=False)
    # password = serializers.PasswordField(max_length=100)
    address = serializers.CharField(max_length=200, required=False)
    city = serializers.CharField(max_length=100, required=False)
    state = serializers.CharField(max_length=100, required=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.address = validated_data.get("address", instance.address)
        instance.city = validated_data.get("city", instance.city)
        instance.state = validated_data.get("state", instance.state)

        instance.save()
        return instance

# ==================================================================================================================

class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model= Stack
        fields = "__all__"

# ==================================================================================================================

class InternSerializer(serializers.ModelSerializer):
    stack = StackSerializer(many=True, read_only=True)
    class Meta:
        model = Intern
        fields = [
            "id",
            "username",
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
        # fields = ['id', 'name', 'logo']
        fields = "__all__"

# ==================================================================================================================

class InternUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = [
            "full_name",
            "state",
            "about",
            "batch",
            "current_salary",
            "is_employed",
            "picture",
        ]

# ==================================================================================================================

class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ["year", "male", "female", "finalist", "participant"]

# ==================================================================================================================

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'