# Generated by Django 4.0.1 on 2022-01-28 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_course_options_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Estudantes'},
        ),
    ]
