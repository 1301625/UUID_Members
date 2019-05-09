# Generated by Django 2.1.7 on 2019-02-22 07:39

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190221_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo_thumbnail',
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='post_photo'),
        ),
    ]
