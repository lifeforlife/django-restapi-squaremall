# Generated by Django 3.0.3 on 2020-02-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='productNo',
            field=models.CharField(max_length=200),
        ),
    ]