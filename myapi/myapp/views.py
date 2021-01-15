from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from myapp.models import Tab
from django.db.models import Sum
from django.http import JsonResponse
import datetime
import json
# Create your views here.

class ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tab.objects.all()

    @action(detail=False, methods=['get'])
    def unblended_cost(self, request, pk=None):
        limit = 5
        
        usageaccountid = request.query_params.get('usageaccountid', None)
        datas = Tab.objects.values(
            "product_productname").annotate(total_cost=Sum("lineitem_unblendedcost")).filter(lineitem_usageaccountid=usageaccountid)
        paginator = Paginator(datas, limit)
        page_number = request.query_params.get('page')
        try:
            list_datas = list(paginator.get_page(page_number))
        except PageNotAnInterger:
            list_datas = list(paginator.get_page(1))
        except EmptyPage:
            list_datas = list(paginator.get_page(1))
        # list_datas = list(datas)
        cost_dict = dict()
        for data in list_datas:
            cost_dict[data['product_productname']] = data['total_cost']
        return JsonResponse(cost_dict)

    @action(detail=False, methods=['get'])
    def usage_amount(self, request, pk=None):
        usageaccountid = request.query_params.get('usageaccountid', None)
        datas = Tab.objects.filter(
            lineitem_usageaccountid=usageaccountid).order_by('product_productname', 'lineitem_usagestartdate')
        use_amount = dict()
        daily_amount = dict()
        for data in datas:
            if data.product_productname not in use_amount:
                use_amount[data.product_productname] = {}

            daily_amount = use_amount[data.product_productname]
            process_day = data.lineitem_usagestartdate.date()
            end_day = data.lineitem_usageenddate.date()
            process_day_str = process_day.strftime('%Y/%m/%d')
            in_one_day_flag = (process_day == end_day)
            while (process_day < end_day or in_one_day_flag):
                if process_day_str in daily_amount:
                    daily_amount[process_day_str] += data.lineitem_usageamount
                else:
                    daily_amount[process_day_str] = data.lineitem_usageamount
                process_day += datetime.timedelta(days=1) 
                process_day_str = process_day.strftime('%Y/%m/%d')
                in_one_day_flag = False
        return JsonResponse(use_amount)
