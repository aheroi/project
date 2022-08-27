# Generated by Django 4.1 on 2022-08-22 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfinpages', '0009_balance_comment_to_notes_income_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'CURRENT'), (2, 'SAVINGS')], default=1),
        ),
        migrations.AlterField(
            model_name='income',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'SALARY'), (2, 'BONUS'), (3, 'OTHER'), (4, 'SAVINGS')], default=1),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'BILLS'), (2, 'GROCERIES'), (3, 'CLOTHES'), (4, 'STUDY'), (5, 'SPORT'), (6, 'FUN'), (7, 'HEALTHY'), (8, 'HOME'), (9, 'FAMILY'), (10, 'GIFT'), (11, 'OTHER'), (12, 'SAVINGS')], default=1),
        ),
    ]