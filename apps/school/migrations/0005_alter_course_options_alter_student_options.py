# Generated by Django 4.0.1 on 2022-01-27 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0004_alter_course_options_alter_student_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={"verbose_name": "Curso", "verbose_name_plural": "Cursos"},
        ),
        migrations.AlterModelOptions(
            name="student",
            options={"verbose_name": "Estudante", "verbose_name_plural": "Estudantes"},
        ),
    ]
