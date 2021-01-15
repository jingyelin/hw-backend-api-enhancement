from rest_framework import serializers
from myapp.models import Tab

class UsageAmountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tab
        fields = ['lineitem_usageamount', 'product_productname', 'lineitem_usagestartdate', 'lineitem_usageenddate']

