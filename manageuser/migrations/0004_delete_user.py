# Generated by Django 3.1 on 2020-09-26 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managegoal', '0003_auto_20200926_1218'),
        ('manageuser', '0003_delete_aaa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
