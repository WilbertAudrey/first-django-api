from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from learning_app.models import User, Topic
from api.serializers import TopicSerializer

class TopicListApiView(APIView):

    def get(self, request, *args, **kwargs):
        topic = Topic.objects.all()
        serializer = TopicSerializer(topic, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self,  request, *args, **kwargs):
        data = {
            'Code' : request.data.get('code'),
            'Name' : request.data.get('name'),
        }
        serializer = TopicSerializer(data = data)
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
