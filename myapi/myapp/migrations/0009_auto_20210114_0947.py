# Generated by Django 3.1.5 on 2021-01-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210114_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tab2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_payeraccountid', models.TextField(blank=True, db_column='bill/PayerAccountId', null=True)),
            ],
            options={
                'db_table': 'tab2',
            },
        ),
        migrations.AlterField(
            model_name='tab1',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]