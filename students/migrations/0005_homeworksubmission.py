# Generated by Django 4.1.7 on 2023-05-06 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('headmaster', '0002_alter_classroom_class_master'),
        ('teacher', '0007_homework_teacher'),
        ('students', '0004_remove_student_teacher_alter_student_current_class_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeworkSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission', models.FileField(upload_to='homework_submissions')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='headmaster.classroom')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.homework')),
            ],
        ),
    ]
