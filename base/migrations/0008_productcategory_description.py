# Generated by Django 3.0.8 on 2020-07-31 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20200731_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]