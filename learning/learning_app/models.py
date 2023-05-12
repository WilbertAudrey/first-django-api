from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.username) + ' ' + str(self.first_name) + ' ' + str(self.last_name)
    
class Category(models.Model):
    category_name = models.CharField(max_length=200, default='Kosong')
    category_description = models.CharField(max_length=500)

    def __str__(self):
        return self.category_name
    
class Lesson(models.Model):
    status_choices = (
        ('Aktif', 'Aktif'),
        ('Tidak Aktif', 'Tidak Aktif'), 
    )

    status_lesson_choices = (
        ('Aktif', 'Aktif'),
        ('Tidak Aktif', 'Tidak Aktif'), 
    )

    lesson_name = models.CharField(max_length= 100)
    category_name = models.ForeignKey(Category,related_name='category_name_lesson', blank=True, null=True, on_delete=models.CASCADE)
    user_create = models.ForeignKey(User, related_name='user_create_lesson', blank=True, null=True, on_delete=models.SET_NULL)
    cesson_description = models.TextField(max_length=200)
    status = models.CharField(max_length=15, choices= status_choices, default= 'Aktif')

    def __str__(self):
        return self.lesson_name
    


class LessonDetail(models.Model):
    lessondetail_name = models.CharField(max_length=100)
    lesson_name = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user_create = models.ForeignKey(User, related_name='user_create_lesson_detail', on_delete=models.CASCADE)
    isi = models.TextField()

    def __str__(self):
        return self.lessondetail_name
    
