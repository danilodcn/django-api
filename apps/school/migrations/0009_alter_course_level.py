# Generated by Django 4.0.1 on 2022-01-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_alter_student_options_alter_student_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('B', 'Basic'), ('I', 'Intermediary'), ('A', 'Advanced')], default='B', max_length=1),
        ),
    ]
