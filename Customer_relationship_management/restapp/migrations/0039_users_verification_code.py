# Generated by Django 4.1.7 on 2023-06-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0038_alter_comment_user_finddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='verification_code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]