# Generated by Django 4.2.14 on 2024-08-14 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
