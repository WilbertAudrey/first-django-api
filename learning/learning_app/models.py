from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username) + ' ' + str(self.first_name) + ' ' + str(self.last_name)


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.PROTECT)
    avatar = models.ImageField(default='default_images/person.jpg',
                               upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField()
    interest = models.CharField(max_length=200, default='Kosong')
    user_create = models.ForeignKey(
        User, related_name='user_create_profile', blank=True, null=True, on_delete=models.SET_NULL)
    user_update = models.ForeignKey(
        User, related_name='user_update_profile', blank=True, null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.first_name) + '' + str(self.user.last_name)

    def save(self, *args, **kwargs):
        super().save()
        try:
            img = Image.open(self.avatar.path)
            if img.height > 200 or img.width > 200:
                new_img = (200, 200)
                img.thumbnail(new_img)
                img.save(self.avatar.path)
        except:
            pass


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

    lesson_name = models.CharField(max_length=100)
    category_name = models.ForeignKey(
        Category, related_name='category_name_lesson', blank=True, null=True, on_delete=models.CASCADE)
    user_create = models.ForeignKey(
        User, related_name='user_create_lesson', blank=True, null=True, on_delete=models.SET_NULL)
    lesson_description = models.TextField(max_length=200)
    status = models.CharField(
        max_length=15, choices=status_choices, default='Aktif')

    def __str__(self):
        return self.lesson_name


class SubLesson(models.Model):
    sublesson_name = models.CharField(max_length=100)
    lesson_name = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user_create = models.ForeignKey(
        User, related_name='user_create_sub_lesson', on_delete=models.CASCADE)
    isi = models.TextField()

    def __str__(self):
        return self.sublesson_name
