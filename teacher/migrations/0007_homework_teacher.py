# Generated by Django 4.1.7 on 2023-05-06 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_homework_classroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher'),
        ),
    ]
