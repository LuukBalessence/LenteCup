# Generated by Django 3.1.7 on 2021-03-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LenteCup', '0005_auto_20210330_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores',
            name='finalscore',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
