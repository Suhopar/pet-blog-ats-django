# Generated by Django 4.2.4 on 2023-10-08 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_absolute_ban_customuser_profile_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='status_ban',
            new_name='usual_ban',
        ),
    ]
