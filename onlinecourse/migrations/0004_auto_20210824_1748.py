# Generated by Django 3.1.3 on 2021-08-24 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_choice_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='course',
            field=models.ManyToManyField(to='onlinecourse.Course'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.TextField(),
        ),
    ]
