# Generated by Django 2.2.6 on 2020-05-14 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20200514_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='meal_type',
            field=models.IntegerField(blank=True, choices=[(1, 'Breakfast'), (2, 'Lunch'), (3, 'Dinner'), (4, 'Snack')], null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='meal_type',
            field=models.IntegerField(blank=True, choices=[(1, 'Breakfast'), (2, 'Lunch'), (3, 'Dinner'), (4, 'Snack')], null=True),
        ),
    ]