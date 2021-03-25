# Generated by Django 3.0.7 on 2021-03-21 07:22

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminUsername', models.CharField(max_length=20, null=True)),
                ('adminPassword', django_cryptography.fields.encrypt(models.CharField(max_length=20, null=True))),
            ],
        ),
    ]
