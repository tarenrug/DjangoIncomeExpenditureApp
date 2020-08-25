# Generated by Django 3.0.8 on 2020-08-25 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeExpenditureStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField(max_length=20)),
                ('other', models.IntegerField(max_length=20)),
                ('mortgage', models.IntegerField(max_length=20)),
                ('rent', models.IntegerField(max_length=20)),
                ('utilites', models.IntegerField(max_length=20)),
                ('travel', models.IntegerField(max_length=20)),
                ('food', models.IntegerField(max_length=20)),
                ('loans', models.IntegerField(max_length=20)),
                ('credit_cards', models.IntegerField(max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]