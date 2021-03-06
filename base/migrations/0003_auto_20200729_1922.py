# Generated by Django 3.0.8 on 2020-07-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200729_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категория товаров',
            },
        ),
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
        migrations.RemoveField(
            model_name='item',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
    ]
