# Generated by Django 3.0.7 on 2021-03-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210321_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderId',
            field=models.CharField(default='5351752838', max_length=10, unique=True),
        ),
    ]
