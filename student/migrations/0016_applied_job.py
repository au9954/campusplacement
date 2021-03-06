# Generated by Django 3.0.1 on 2020-05-04 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_company_last_date_to_apply'),
        ('student', '0015_auto_20200504_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applied_Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
                ('student', models.ManyToManyField(to='student.Student')),
            ],
        ),
    ]
