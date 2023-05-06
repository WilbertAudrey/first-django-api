from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.username) + ' ' + str(self.first_name) + ' ' + str(self.last_name)
    
class Topic(models.Model):
    status_choices = (
        ('Aktif', 'Aktif'),
        ('Tidak Aktif', 'Tidak Aktif'), 
    )

    status_topic_choices = (
        ('On Going','On Going'),
        ('Finished', 'Finished'),
    )

    Code = models.CharField(max_length= 200)
    Name = models.CharField(max_length= 100)
    status = models.CharField(max_length=15, choices= status_choices, default= 'Aktif')
    user_create = models.ForeignKey(User, related_name= 'user_create_table_resto', blank = True, null = True, on_delete= models.SET_NULL)
    user_create = models.ForeignKey(User, related_name= 'user_update_table_resto', blank = True, null = True, on_delete= models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add= True)
    last_modified = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.Name