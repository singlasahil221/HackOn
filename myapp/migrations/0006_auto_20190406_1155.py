# Generated by Django 2.0.12 on 2019-04-06 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20190405_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubmission',
            name='status',
            field=models.CharField(choices=[('AC', 'accepted'), ('WA', 'wrong')], max_length=100),
        ),
    ]
