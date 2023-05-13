from django.contrib import admin
from .models import User, Lesson, Category, SubLesson

admin.site.register(User)
admin.site.register(Lesson)
admin.site.register(Category)
admin.site.register(SubLesson)
# Register your models here.
