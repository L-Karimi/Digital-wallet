# Generated by Django 4.0.6 on 2022-07-29 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Gender',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Phone_Number',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='nationality',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
