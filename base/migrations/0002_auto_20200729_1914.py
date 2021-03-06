# Generated by Django 3.0.8 on 2020-07-29 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Категория товара', 'verbose_name_plural': 'Категория товаров'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='des',
        ),
        migrations.RemoveField(
            model_name='item',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='item',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]
