from rest_framework import serializers
from learning_app.models import (
    User, Lesson,Category, LessonDetail
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
        fields = ('id', 'Lesson_code', 'Lesson_name', 'Lesson_description','status')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'Category_code', 'Category_name', 'Category_description')

class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonDetail
        fields = ('id', 'nama_subjudul', 'Lesson_name', 'isi')

