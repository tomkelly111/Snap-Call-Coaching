# Generated by Django 3.2.22 on 2023-11-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_coach_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='featured_image',
            field=models.ImageField(default='placeholder', upload_to='', verbose_name='image'),
        ),
    ]