# Generated by Django 3.2.3 on 2021-06-23 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientside', '0040_commande_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='User',
        ),
        migrations.AddField(
            model_name='commande',
            name='User',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='auth.user'),
            preserve_default=False,
        ),
    ]
