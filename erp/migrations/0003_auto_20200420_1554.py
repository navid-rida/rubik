# Generated by Django 2.2.12 on 2020-04-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_auto_20200401_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='advance',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='later_payment',
        ),
        migrations.AddField(
            model_name='quotation',
            name='advance_percent',
            field=models.DecimalField(decimal_places=2, default=50, max_digits=5, verbose_name='Advance Payment(percent)'),
            preserve_default=False,
        ),
    ]
