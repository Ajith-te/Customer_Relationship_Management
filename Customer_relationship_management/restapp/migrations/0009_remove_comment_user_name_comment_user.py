# Generated by Django 4.1.7 on 2023-05-24 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restapp', '0008_remove_comment_user_comment_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]