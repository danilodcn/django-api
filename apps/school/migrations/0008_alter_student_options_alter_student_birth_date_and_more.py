# Generated by Django 4.0.1 on 2022-01-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0007_alter_student_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student",
            options={"verbose_name": "Student", "verbose_name_plural": "Students"},
        ),
        migrations.AlterField(
            model_name="student",
            name="birth_date",
            field=models.DateField(verbose_name="birth date"),
        ),
        migrations.AlterField(
            model_name="student",
            name="name",
            field=models.CharField(max_length=40, verbose_name="name"),
        ),
    ]
