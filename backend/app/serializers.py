from django.db import models
from rest_framework import serializers

from .models import *


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
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)

        instance.save()
        return instance
    

class InternSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=100,required=False)
    stack = serializers.CharField(max_length = 100,required=False)
    job = serializers.CharField(max_length=100,required=False)
    batch = serializers.IntegerField(required=False)

    

    def create(self, validated_data):
        return Intern.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.stack = validated_data.get('stack', instance.stack)
        instance.job = validated_data.get('job', instance.job)
        instance.batch = validated_data.get('batch', instance.batch)

        instance.save()
        return instance

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ['job_title', 'company_name','gotten_at', 'last_updated_at', 'job_description', 'currently_active']



class UpdateInternSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
