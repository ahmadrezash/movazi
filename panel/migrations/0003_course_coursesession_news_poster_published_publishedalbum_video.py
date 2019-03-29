# Generated by Django 2.1.7 on 2019-03-26 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panel', '0002_auto_20190326_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=300)),
                ('format', models.CharField(max_length=200)),
                ('summery', models.TextField()),
                ('speaker', models.CharField(max_length=200)),
                ('session', models.IntegerField()),
                ('holding_loc', models.CharField(max_length=200)),
                ('holding_date', models.DateField(auto_now_add=True)),
                ('audience', models.CharField(max_length=200)),
                ('scientific_level', models.CharField(max_length=200)),
                ('prerequisite', models.CharField(max_length=200)),
                ('table_of_content', models.CharField(max_length=200)),
                ('resources', models.FileField(upload_to='Courses/resourses')),
                ('image_index', models.ImageField(height_field=100, upload_to='image/Courses/index', width_field=100)),
                ('tags', models.CharField(max_length=300)),
                ('image_perview', models.ImageField(height_field=100, upload_to='image/Courses/preview', width_field=100)),
                ('slug', models.CharField(max_length=300)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Category')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=300)),
                ('summery', models.TextField()),
                ('speaker', models.CharField(max_length=200)),
                ('time', models.TimeField()),
                ('audience', models.CharField(max_length=200)),
                ('table_of_content', models.CharField(max_length=200)),
                ('resources', models.FileField(upload_to='Courses/resourses')),
                ('image_index', models.ImageField(height_field=100, upload_to='image/Courses/index', width_field=100)),
                ('tags', models.CharField(max_length=300)),
                ('image_perview', models.ImageField(height_field=100, upload_to='image/Courses/preview', width_field=100)),
                ('slug', models.CharField(max_length=300)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Course')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Category')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=300)),
                ('summery', models.TextField()),
                ('full_text', models.TextField()),
                ('slug', models.CharField(max_length=300)),
                ('image', models.ImageField(height_field=100, upload_to='image/profile', width_field=100)),
                ('tags', models.CharField(max_length=300)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=300)),
                ('discription', models.TextField()),
                ('slug', models.CharField(max_length=300)),
                ('image', models.ImageField(height_field=100, upload_to='poster', width_field=100)),
                ('preview', models.ImageField(height_field=100, upload_to='preview/poster', width_field=100)),
                ('tags', models.CharField(max_length=300)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Published',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=300)),
                ('subject', models.CharField(max_length=200)),
                ('summery', models.TextField()),
                ('full_text', models.TextField()),
                ('source', models.URLField(blank=True, db_index=True, max_length=128)),
                ('publishing_date', models.DateField(auto_now_add=True)),
                ('image_index', models.ImageField(height_field=100, upload_to='image/Published/index', width_field=100)),
                ('image_cover', models.ImageField(height_field=100, upload_to='image/Published/cover', width_field=100)),
                ('tags', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Category')),
            ],
        ),
        migrations.CreateModel(
            name='PublishedAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=300)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Published')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=300)),
                ('discription', models.TextField()),
                ('slug', models.CharField(max_length=300)),
                ('image', models.ImageField(height_field=100, upload_to='video', width_field=100)),
                ('preview', models.ImageField(height_field=100, upload_to='preview/video', width_field=100)),
                ('time', models.TimeField()),
                ('tags', models.CharField(max_length=300)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
