# Generated by Django 3.1.5 on 2021-01-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210114_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab1',
            name='lineitem_usageenddate',
            field=models.DateTimeField(blank=True, db_column='lineItem/UsageEndDate', null=True),
        ),
        migrations.AlterField(
            model_name='tab1',
            name='lineitem_usagestartdate',
            field=models.DateTimeField(blank=True, db_column='lineItem/UsageStartDate', null=True),
        ),
    ]
