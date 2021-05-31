# Generated by Django 3.2 on 2021-05-29 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientside', '0006_auto_20210529_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childcategory',
            name='Article',
        ),
        migrations.AddField(
            model_name='article',
            name='childcategory',
            field=models.ForeignKey(default=1, max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='ArticleChildCategory', to='clientside.childcategory'),
        ),
    ]
