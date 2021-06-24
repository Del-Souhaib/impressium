# Generated by Django 3.2.3 on 2021-06-04 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientside', '0022_alter_specification_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='Quantity',
            field=models.ManyToManyField(blank=True, related_name='QuantitySpecification', to='clientside.Quantity', verbose_name='Quantite'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='customQuantite',
            field=models.BooleanField(blank=True, null=True, verbose_name='client choisi Quantite'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='customSize',
            field=models.BooleanField(blank=True, null=True, verbose_name='client choisi longeur et largeur'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='finition',
            field=models.ManyToManyField(blank=True, related_name='FinitionSpecification', to='clientside.Finition', verbose_name='Finition'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='fontColor',
            field=models.ManyToManyField(blank=True, related_name='FontColorSpecification', to='clientside.FontColor', verbose_name='Font coleur'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='orientation',
            field=models.ManyToManyField(blank=True, related_name='OrientationSpecification', to='clientside.Orientation', verbose_name='Orientation'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='paperColor',
            field=models.ManyToManyField(blank=True, related_name='PaperColorSpecification', to='clientside.PaperColor', verbose_name='Papier coleur'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='paperType',
            field=models.ManyToManyField(blank=True, related_name='PaperSpecification', to='clientside.PaperType', verbose_name='Papier type'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='side',
            field=models.ManyToManyField(blank=True, related_name='SideSpecification', to='clientside.Side', verbose_name='direction'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='size',
            field=models.ManyToManyField(blank=True, related_name='SizeSpecification', to='clientside.Size1', verbose_name='Size'),
        ),
    ]