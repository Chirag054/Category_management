# Generated by Django 3.2.2 on 2021-05-07 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='cat_name',
            field=models.CharField(max_length=200),
        ),
    ]