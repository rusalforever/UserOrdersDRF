# Generated by Django 2.2.7 on 2019-11-13 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191112_1608'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('first_name', 'last_name', 'date_birthday')},
        ),
    ]
