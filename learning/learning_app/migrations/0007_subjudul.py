# Generated by Django 4.2.1 on 2023-05-11 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_app', '0006_category_lesson_delete_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubJudul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_subjudul', models.CharField(max_length=100)),
                ('isi', models.TextField()),
                ('lesson_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_app.lesson')),
            ],
        ),
    ]