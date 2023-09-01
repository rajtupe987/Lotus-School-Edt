# Generated by Django 4.2.4 on 2023-09-01 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotusedt', '0008_studentmodel_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotusedt.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotusedt.department')),
                ('students', models.ManyToManyField(to='lotusedt.studentmodel')),
            ],
        ),
    ]
