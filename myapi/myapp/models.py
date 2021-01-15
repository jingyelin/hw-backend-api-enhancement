from django.db import models

# Create your models here.

class Tab(models.Model):
    field1 = models.AutoField(primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    bill_payeraccountid = models.TextField(
        db_column='bill/PayerAccountId', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    lineitem_usageaccountid = models.TextField(
        db_column='lineItem/UsageAccountId', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    lineitem_usagestartdate = models.DateTimeField(
        db_column='lineItem/UsageStartDate', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    lineitem_usageenddate = models.DateTimeField(
        db_column='lineItem/UsageEndDate', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    lineitem_usageamount = models.DecimalField(max_digits=30, decimal_places=12,
        db_column='lineItem/UsageAmount', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    lineitem_unblendedrate = models.FloatField(
        db_column='lineItem/UnblendedRate', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    lineitem_unblendedcost = models.DecimalField(max_digits=30, decimal_places=12,
        db_column='lineItem/UnblendedCost', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    product_productname = models.TextField(
        db_column='product/ProductName', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab'

