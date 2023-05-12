from django.urls import path, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    LessonListApiView, CategoryListApiView, LessonDetailListApiView
)
app_name = 'api'
urlpatterns = [
    # path('api/v1/login', LoginView.as_view())
    # path('api/v1/logout', LogoutView.as_view())
    # path('api/v1/register', RegisterView.as_view())
    path('api/lesson', views.LessonListApiView.as_view()),
    path('api/category', views.CategoryListApiView.as_view()),
    path('api/subjudul', views.LessonDetailListApiView.as_view()),
]