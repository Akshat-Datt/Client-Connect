# Generated by Django 4.2 on 2024-04-05 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='sales',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]