# Generated by Django 4.0.6 on 2023-06-10 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_post_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='api/images/'),
        ),
    ]
