# Generated by Django 4.2 on 2023-06-11 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_course_student_paid_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_course_fee',
            old_name='student_id',
            new_name='user',
        ),
    ]
