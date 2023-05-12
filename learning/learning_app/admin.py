from django.contrib import admin
from .models import User, Lesson, Category, LessonDetail

admin.site.register(User)
admin.site.register(Lesson)
admin.site.register(Category)
admin.site.register(LessonDetail)
# Register your models here.
