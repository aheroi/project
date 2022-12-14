# Generated by Django 4.1 on 2022-08-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'CURRENT'), (2, 'SAVING')], default=1)),
                ('notes', models.CharField(default='-', max_length=64)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'balances',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'SALARY'), (2, 'BONUS'), (3, 'OTHER')], default=1)),
                ('notes', models.CharField(default='-', max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'incomes',
            },
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'BILLS'), (2, 'GROCERIES'), (3, 'CLOTHES'), (4, 'STUDY'), (5, 'SPORT'), (6, 'FUN'), (7, 'HEALTHY'), (8, 'HOME'), (9, 'FAMILY'), (10, 'GIFT'), (11, 'OTHER'), (12, 'SAVING')], default=1)),
                ('notes', models.CharField(default='-', max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'outcomes',
            },
        ),
    ]
