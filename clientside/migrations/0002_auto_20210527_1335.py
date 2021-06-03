# Generated by Django 3.2 on 2021-05-27 12:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientside', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='ChildCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ChildCategory', to='clientside.category')),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='type',
        ),
        migrations.RemoveField(
            model_name='search',
            name='user_id',
        ),
        migrations.AddField(
            model_name='search',
            name='user',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='search_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='TopRecherch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('ChildCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TopRecherChildCategory', to='clientside.childcategory')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='childcategory',
            field=models.ForeignKey(default=1, max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='ArticleChildCategory', to='clientside.childcategory'),
            preserve_default=False,
        ),
    ]