# Generated by Django 3.1.5 on 2021-01-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20210114_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tab2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_payeraccountid', models.TextField(blank=True, db_column='PayerAccountId', null=True)),
            ],
            options={
                'db_table': 'tab2',
            },
        ),
        migrations.DeleteModel(
            name='Tab3',
        ),
    ]
