# Generated by Django 3.2.4 on 2021-07-03 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0007_auto_20210704_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addres',
            name='city',
            field=models.CharField(max_length=100, verbose_name='City Name'),
        ),
        migrations.AlterField(
            model_name='addres',
            name='medicinedate',
            field=models.CharField(max_length=100, verbose_name='Medicine Expiration Date'),
        ),
        migrations.AlterField(
            model_name='addres',
            name='medicineqty',
            field=models.CharField(max_length=100, verbose_name='Medicine Quantity'),
        ),
        migrations.AlterField(
            model_name='addres',
            name='medicinetype',
            field=models.CharField(max_length=100, verbose_name='Medicine Quantity Type'),
        ),
    ]
