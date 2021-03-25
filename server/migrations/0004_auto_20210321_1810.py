# Generated by Django 3.0.7 on 2021-03-21 12:40

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20210321_1759'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServerAuth',
        ),
        migrations.RemoveField(
            model_name='serverdetails',
            name='serverurl',
        ),
        migrations.AddField(
            model_name='serverdetails',
            name='adminPassword',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=20, null=True)),
        ),
        migrations.AddField(
            model_name='serverdetails',
            name='adminUsername',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=20, null=True)),
        ),
        migrations.AddField(
            model_name='serverdetails',
            name='server_url',
            field=models.URLField(null=True),
        ),
    ]
