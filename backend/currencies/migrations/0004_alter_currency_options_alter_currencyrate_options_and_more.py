# Generated by Django 4.2.4 on 2023-08-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0003_alter_currencyrate_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'Валюта', 'verbose_name_plural': 'Валюты'},
        ),
        migrations.AlterModelOptions(
            name='currencyrate',
            options={'verbose_name': 'Курс валюты', 'verbose_name_plural': 'Курсы Валют'},
        ),
        migrations.AlterField(
            model_name='currencyrate',
            name='date',
            field=models.DateField(verbose_name='Дата сбора данных'),
        ),
        migrations.AlterField(
            model_name='currencyrate',
            name='value',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Курс'),
        ),
        migrations.AlterUniqueTogether(
            name='currency',
            unique_together={('char_code', 'name')},
        ),
    ]