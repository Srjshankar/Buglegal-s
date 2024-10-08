# Generated by Django 4.2.4 on 2024-01-08 11:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ehrms', '0088_typeofplans_price_for_annual_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip_request',
            name='companyid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ehrms.companys'),
        ),
        migrations.AlterField(
            model_name='addonsuser',
            name='date',
            field=models.DateField(default=datetime.date(2024, 1, 8)),
        ),
        migrations.AlterField(
            model_name='adminhod',
            name='dateofbirth',
            field=models.DateField(default=datetime.date(2024, 1, 8)),
        ),
        migrations.AlterField(
            model_name='adminhod',
            name='dateofjoining',
            field=models.DateField(default=datetime.date(2024, 1, 8)),
        ),
        migrations.AlterField(
            model_name='employ_payslip',
            name='dateofbirth',
            field=models.DateField(default=datetime.date(2024, 1, 8)),
        ),
        migrations.AlterField(
            model_name='employeeloginlogout',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 8, 17, 27, 24, 866605)),
        ),
        migrations.AlterField(
            model_name='employs',
            name='dateofjoining',
            field=models.DateField(default=datetime.date(2024, 1, 8)),
        ),
        migrations.AlterField(
            model_name='hr',
            name='dateofbirth',
            field=models.DateField(default=datetime.date(2024, 1, 8)),
        ),
        migrations.AlterField(
            model_name='hr',
            name='dateofjoining',
            field=models.DateField(default=datetime.date(2024, 1, 8)),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='task_date',
            field=models.DateField(default=datetime.date(2024, 1, 8)),
        ),
        migrations.AlterField(
            model_name='tlassigntask',
            name='task_date',
            field=models.DateField(default=datetime.date(2024, 1, 8)),
        ),
    ]
