# Generated by Django 4.1 on 2022-08-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfinpages', '0007_balance_user_income_user_outcome_comment_to_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='notes',
            field=models.CharField(default='--', max_length=255),
        ),
    ]