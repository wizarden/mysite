# Generated by Django 3.0.8 on 2020-08-04 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_productcategory_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategory',
            old_name='image',
            new_name='category_image',
        ),
    ]
