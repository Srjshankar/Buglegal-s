# Generated by Django 4.2.4 on 2023-12-26 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehrms', '0062_typeofplans_employe_limit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeloginlogout',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 10, 29, 29, 814921)),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='task_date',
            field=models.DateField(default=datetime.date(2023, 12, 26)),
        ),
        migrations.AlterField(
            model_name='tlassigntask',
            name='task_date',
            field=models.DateField(default=datetime.date(2023, 12, 26)),
        ),
    ]
