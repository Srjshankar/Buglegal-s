# Generated by Django 4.2.4 on 2023-11-29 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehrms', '0004_alter_employs_dateofbirth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employs',
            name='dateofbirth',
        ),
    ]
