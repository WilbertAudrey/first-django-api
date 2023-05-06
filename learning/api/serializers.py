from rest_framework import serializers
from learning_app.models import (
    User, Topic,
)
from django.contrib.auth import authenticate
from rest_framework import exceptions
from django.core.exceptions import ValidationError
from django.http import HttpRequest, JsonResponse
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'Code', 'Name', 'status')

