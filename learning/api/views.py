from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from learning_app.models import User, Lesson, Category, SubLesson, Profile
from api.serializers import LessonSerializer, CategorySerializer, SubLessonSerializer, ProfileSerializer


class LessonListApiView(APIView):

    def get(self, request, *args, **kwargs):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,  request, *args, **kwargs):
        data = {
            'Lesson code': request.data.get('Lesson_code'),
            'Lesson name': request.data.get('Lesson_name'),
            'status': request.data.get('status'),
        }
        serializer = LessonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_201_CREATED,
                'message': 'Data created successfully...',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class CategoryListApiView(APIView):

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,  request, *args, **kwargs):
        data = {
            'category code': request.data.get('category_code'),
            'category name': request.data.get('category_name'),
            'category_description': request.data.get('category_description'),
        }
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_201_CREATED,
                'message': 'Data created successfully...',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class SubLessonListApiView(APIView):

    def get(self, request, *args, **kwargs):
        sublesson = SubLesson.objects.all()
        serializer = SubLessonSerializer(sublesson, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,  request, *args, **kwargs):
        data = {
            'sub lesson name': request.data.get('sublesson_name'),
            'lesson name': request.data.get('lesson_name'),
            'isi': request.data.get('isi'),
        }
        serializer = SubLessonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_201_CREATED,
                'message': 'Data created successfully...',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailAPI(APIView):
    def get_object(self, user_id):
        try:
            return Profile.objects.get(user=user_id)
        except Profile.DoesNotExist:
            return None

    def get(self, request, user_id, *args, **kwargs):
        profile_instance = self.get_object(user_id)
        if not profile_instance:
            return Response(
                {'response': "Data does not exists..."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProfileSerializer(profile_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Pertemuan 6
