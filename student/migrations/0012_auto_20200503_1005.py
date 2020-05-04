# Generated by Django 3.0.1 on 2020-05-03 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20200503_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', help_text='Please upload your recent photograph', upload_to='student_images/%Y/%m/%d/'),
        ),
    ]
