# Generated by Django 4.1.3 on 2022-12-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_certificate_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
