# Generated by Django 4.2.1 on 2023-06-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_reel_transactions_reel_time_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reel_entry',
            name='reel_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
