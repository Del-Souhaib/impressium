# Generated by Django 3.2.3 on 2021-06-30 15:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientside', '0046_auto_20210630_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='Article',
        ),
        migrations.AddField(
            model_name='commande',
            name='Pane',
            field=models.ManyToManyField(related_name='panes', to='clientside.Pane'),
        ),
        migrations.CreateModel(
            name='LastPane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ArticleDesign', models.FileField(null=True, upload_to='static/pane_images', verbose_name='Nom')),
                ('CostumQuantity', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('FileControle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FileControleLastPane', to='clientside.filecontrole')),
                ('Quantity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='QuantityLastPane', to='clientside.quantity', verbose_name='Quantite')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ArticleLastPane', to='clientside.article')),
                ('delevery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DeleveryLastPane', to='clientside.delivery')),
                ('finition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FinitionLastPane', to='clientside.finition', verbose_name='Finition')),
                ('fontColor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FontColorLastPane', to='clientside.fontcolor', verbose_name='Font coleur')),
                ('formattype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FormaTypeLastPane', to='clientside.formattype', verbose_name='Forma type')),
                ('orientation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OrientationLastPane', to='clientside.orientation', verbose_name='Orientation')),
                ('paperColor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PaperColorLastPane', to='clientside.papercolor', verbose_name='Papier coleur')),
                ('paperType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PaperLastPane', to='clientside.papertype', verbose_name='Papier type')),
                ('side', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SideLastPane', to='clientside.side', verbose_name='direction')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SizeLastPane', to='clientside.size1', verbose_name='Size')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserLastPane', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]