# Generated by Django 4.2.4 on 2023-09-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_post_likes_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('hidden', 'Hidden')], default='published', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('hidden', 'Hidden')], default='published', max_length=10),
        ),
    ]