# Generated by Django 4.2.1 on 2023-06-10 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_reel_byweight_alter_reel_entry_reel_gsm_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reel_byweight',
            old_name='reel_gsm',
            new_name='GSM',
        ),
        migrations.RenameField(
            model_name='reel_byweight',
            old_name='reel_weight',
            new_name='Total_weight',
        ),
    ]