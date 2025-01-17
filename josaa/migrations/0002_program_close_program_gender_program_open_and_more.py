# Generated by Django 4.2.2 on 2023-06-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josaa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='close',
            field=models.IntegerField(default=99999),
        ),
        migrations.AddField(
            model_name='program',
            name='gender',
            field=models.CharField(default='Gender-Neutral', max_length=200),
        ),
        migrations.AddField(
            model_name='program',
            name='open',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='program',
            name='roundd',
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name='program',
            name='seat_type',
            field=models.CharField(default='OPEN', max_length=200),
        ),
        migrations.AddField(
            model_name='program',
            name='year',
            field=models.IntegerField(default=2020),
        ),
    ]
