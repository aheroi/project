# Generated by Django 4.1 on 2022-08-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfinpages', '0005_income_comment_to_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='notes',
            field=models.CharField(default='--', max_length=255),
        ),
    ]