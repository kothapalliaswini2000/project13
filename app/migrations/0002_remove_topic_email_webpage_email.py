# Generated by Django 5.0.3 on 2024-04-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='email',
        ),
        migrations.AddField(
            model_name='webpage',
            name='email',
            field=models.EmailField(default='ashu@gmail.com', max_length=254),
        ),
    ]
