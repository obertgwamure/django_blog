# Generated by Django 4.2 on 2023-05-30 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('1', 'Software Development'), ('2', 'Cybersecurity'), ('3', 'Tech in Africa'), ('4', 'Python'), ('5', 'Django'), ('6', 'JavaScript'), ('7', 'HTML and CSS'), ('8', 'Tutorials'), ('9', 'General Tech'), ('10', 'Industry-Specific Tech')], max_length=240)),
                ('slug', models.SlugField(default='django-db-models-fields-CharField', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('Comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcomments', to='blog.comment')),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240)),
                ('body', models.TextField(blank=True)),
                ('slug', models.SlugField(default='django-db-models-fields-CharField', unique=True)),
                ('image', models.ImageField(blank=True, max_length=1000, upload_to='post_image_path')),
                ('status', models.CharField(choices=[('complete', 'complete'), ('draft', 'draft')], default='draft', max_length=15)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_edited', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default='General Tech', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.category')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
    ]
