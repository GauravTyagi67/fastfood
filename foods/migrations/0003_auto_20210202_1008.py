# Generated by Django 3.0.11 on 2021-02-02 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_auto_20210202_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='pImage',
            field=models.URLField(),
        ),
    ]
