# Generated by Django 4.2 on 2023-05-12 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_app', '0009_lessondetail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sublesson_name', models.CharField(max_length=100)),
                ('isi', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='cesson_description',
            new_name='lesson_description',
        ),
        migrations.DeleteModel(
            name='LessonDetail',
        ),
        migrations.AddField(
            model_name='sublesson',
            name='lesson_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_app.lesson'),
        ),
        migrations.AddField(
            model_name='sublesson',
            name='user_create',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_create_sub_lesson', to=settings.AUTH_USER_MODEL),
        ),
    ]
