# Generated by Django 3.2.22 on 2023-11-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_testimonials_options'),
        ('profiles', '0003_userprofile_default_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='reviewed_courses',
            field=models.ManyToManyField(blank=True, related_name='reviewed_courses', to='courses.Course'),
        ),
    ]
