# Generated by Django 4.2 on 2023-06-03 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_stydent_course_fee_student_course_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_student',
            name='paid_amount',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]