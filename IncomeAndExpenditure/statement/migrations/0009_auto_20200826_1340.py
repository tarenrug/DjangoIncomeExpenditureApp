# Generated by Django 3.0.8 on 2020-08-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statement', '0008_auto_20200826_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomeexpenditurestatement',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]