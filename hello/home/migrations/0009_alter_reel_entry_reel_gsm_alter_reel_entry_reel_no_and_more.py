# Generated by Django 4.2.1 on 2023-06-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_reel_entry_reel_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reel_entry',
            name='reel_gsm',
            field=models.DecimalField(decimal_places=2, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='reel_entry',
            name='reel_no',
            field=models.DecimalField(decimal_places=2, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='reel_entry',
            name='reel_size',
            field=models.DecimalField(decimal_places=2, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='reel_entry',
            name='reel_weight',
            field=models.DecimalField(decimal_places=2, max_digits=30, null=True),
        ),
    ]
