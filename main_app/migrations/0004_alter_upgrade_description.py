# Generated by Django 4.1.7 on 2023-03-31 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_upgrade_alter_updates_options_alter_updates_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upgrade',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]