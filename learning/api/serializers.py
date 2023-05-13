from rest_framework import serializers
from learning_app.models import (
    User, Profile, Lesson,Category, SubLesson
)
from django.contrib.auth import authenticate
from rest_framework import exceptions
from django.core.exceptions import ValidationError
from django.http import HttpRequest, JsonResponse
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id','lesson_name', 'category_name', 'lesson_description','status')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','category_name', 'category_description')

class SubLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubLesson
        fields = ('id', 'sublesson_name', 'lesson_name', 'isi')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'avatar', 'bio', 'interest')