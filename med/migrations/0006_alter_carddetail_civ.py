# Generated by Django 3.2.4 on 2021-07-01 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0005_alter_carddetail_civ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddetail',
            name='civ',
            field=models.PositiveIntegerField(verbose_name='CVV'),
        ),
    ]