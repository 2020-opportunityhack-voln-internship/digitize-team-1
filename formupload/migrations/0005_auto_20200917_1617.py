# Generated by Django 2.2.13 on 2020-09-17 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formupload', '0004_auto_20200917_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperform',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]