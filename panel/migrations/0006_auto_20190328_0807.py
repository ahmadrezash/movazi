# Generated by Django 2.1.7 on 2019-03-28 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_auto_20190327_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poster',
            name='preview',
        ),
        migrations.AddField(
            model_name='poster',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='panel.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publishedalbum',
            name='image',
            field=models.ImageField(default=1, upload_to='image/Published/Album'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='panel.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/Article'),
        ),
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(upload_to='image/profile'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image_index',
            field=models.ImageField(upload_to='image/Courses/index'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image_perview',
            field=models.ImageField(upload_to='image/Courses/preview'),
        ),
        migrations.AlterField(
            model_name='coursesession',
            name='image_index',
            field=models.ImageField(upload_to='image/Courses/index'),
        ),
        migrations.AlterField(
            model_name='coursesession',
            name='image_perview',
            field=models.ImageField(upload_to='image/Courses/preview'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='image/News'),
        ),
        migrations.AlterField(
            model_name='poster',
            name='image',
            field=models.ImageField(upload_to='poster'),
        ),
        migrations.AlterField(
            model_name='published',
            name='image_cover',
            field=models.ImageField(upload_to='image/Published/cover'),
        ),
        migrations.AlterField(
            model_name='published',
            name='image_index',
            field=models.ImageField(upload_to='image/Published/index'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(upload_to='video'),
        ),
        migrations.AlterField(
            model_name='video',
            name='preview',
            field=models.ImageField(upload_to='preview/video'),
        ),
    ]
