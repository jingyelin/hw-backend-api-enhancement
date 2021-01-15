# Generated by Django 3.1.5 on 2021-01-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tab1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_payeraccountid', models.TextField(blank=True, db_column='bill/PayerAccountId', null=True)),
                ('lineitem_usageaccountid', models.TextField(blank=True, db_column='lineItem/UsageAccountId', null=True)),
                ('lineitem_usagestartdate', models.DateTimeField(blank=True, db_column='lineItem/UsageStartDate', null=True)),
                ('lineitem_usageenddate', models.DateTimeField(blank=True, db_column='lineItem/UsageEndDate', null=True)),
                ('lineitem_usageamount', models.FloatField(blank=True, db_column='lineItem/UsageAmount', null=True)),
                ('lineitem_unblendedrate', models.FloatField(blank=True, db_column='lineItem/UnblendedRate', null=True)),
                ('lineitem_unblendedcost', models.FloatField(blank=True, db_column='lineItem/UnblendedCost', null=True)),
                ('product_productname', models.TextField(blank=True, db_column='product/ProductName', null=True)),
            ],
            options={
                'db_table': 'tab1',
            },
        ),
    ]
