# Generated by Django 2.1.7 on 2019-03-26 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=300)),
                ('summery', models.TextField()),
                ('full_text', models.TextField()),
                ('source', models.URLField(blank=True, db_index=True, max_length=128)),
                ('slug', models.CharField(max_length=300)),
                ('image', models.ImageField(height_field=100, upload_to='image/profile', width_field=100)),
                ('tags', models.CharField(max_length=300)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('gender', models.BooleanField()),
                ('birth_date', models.DateField()),
                ('avatar', models.ImageField(height_field=100, upload_to='image/profile', width_field=100)),
                ('last_update', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_english', models.CharField(max_length=100)),
                ('name_persian', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Category'),
        ),
    ]
