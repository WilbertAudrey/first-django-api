from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from learning_app.models import User, Lesson, Category, LessonDetail
from api.serializers import LessonSerializer, CategorySerializer, LessonDetailSerializer

class LessonListApiView(APIView):

    def get(self, request, *args, **kwargs):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self,  request, *args, **kwargs):
        data = {
            'Lesson code' : request.data.get('Lesson_code'),
            'Lesson name' : request.data.get('Lesson_name'),
            'status' : request.data.get('status'),
        }
        serializer = LessonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status' : status.HTTP_201_CREATED,
                'message' : 'Data created successfully...',
                'data' : serializer.data
            }
            return Response(response, status = status.HTTP_201_CREATED)

        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

class CategoryListApiView(APIView):

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self,  request, *args, **kwargs):
        data = {
            'category code' : request.data.get('category_code'),
            'category name' : request.data.get('category_name'),
            'category_description' : request.data.get('category_description'),
        }
        serializer = CategorySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status' : status.HTTP_201_CREATED,
                'message' : 'Data created successfully...',
                'data' : serializer.data
            }
            return Response(response, status = status.HTTP_201_CREATED)

        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    
class LessonDetailListApiView(APIView):

    def get(self, request, *args, **kwargs):
        lessondetail = LessonDetail.objects.all()
        serializer = LessonDetailSerializer(lessondetail, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self,  request, *args, **kwargs):
        data = {
            'lesson detail name' : request.data.get('lessondetail_name'),
            'lesson name' : request.data.get('lesson_name'),
            'isi' : request.data.get('isi'),
        }
        serializer = LessonDetailSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status' : status.HTTP_201_CREATED,
                'message' : 'Data created successfully...',
                'data' : serializer.data
            }
            return Response(response, status = status.HTTP_201_CREATED)

        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)


# Pertemuan 6 
