# Generated by Django 3.1 on 2020-10-03 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managegoal', '0007_auto_20200929_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]
