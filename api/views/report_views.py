from decimal import Decimal
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser 
from django.db.models import (F, Sum)
from due.models import Due, Due_Definition
from category.models import Category
from due.models import Due, Due_Definition
from savings.models import Receive, Saved_Money
from ..serializers.due_serializers import DueSerializer, DueDefinitionSerializer 
from ..serializers.savings_serializers import ReceiveSerializer
import datetime

from datetime import date, timedelta
import calendar


def total_dues_month(due, date, total_dues, items):
    time_end = getattr(due, 'time_end')
    if time_end is None or time_end > date:
        total_dues = total_dues + getattr(due, 'value')
    
    items.append({
        "id": getattr(due, 'id'),
        "description": getattr(due.due, 'due_description'),
        "value": getattr(due, 'value')
    })
    
    return total_dues, items


def total_receives_month(receives, date, total_receive, receives_month):
    time_end = getattr(receives, 'time_end')
    if time_end is None or time_end > date:
        total_receive = total_receive + getattr(receives, 'value')

    receives_month.append({
        "description": getattr(receives, 'description'),
        "value": str(getattr(receives, 'value'))
    })
    return total_receive, receives_month

def total_savings():
    # buscar o total de dinheiro guardado, savings, usando a data de aplicação e retirada?
    savings = Saved_Money.objects.all()
        


def report(request):
    if request.method == "GET":
        dues = Due_Definition.objects.all()
        receives = Receive.objects.all()
        sum_dues = Due_Definition.objects.aggregate(total_dues=Sum('value'))
        sum_receives = Receive.objects.aggregate(total_receives=Sum('value'))
        sum_save = Saved_Money.objects.aggregate(total_save=Sum('value'))

        serializer = ReceiveSerializer(data=receives, many=True)

        print(serializer)
        #total_month = sum_dues['total_dues'] + sum_receives['total_receives']

        ###
        ###    Percorrer 12 meses (os que vão ser listados de inicio)
        ###    Verificar se a data final da divida é maior ou igual ao mês do indice
        ###        se for a divida é somada com as outras 
        ###

        date_current = datetime.date.today()
        # mounth_current = date_current.strftime("%m")
        print(sum_save['total_save'])
        total = []
        total_month = 0
        all_total = sum_save['total_save']
        for i in range(5):
            total_dues = 0
            total_receive = 0
            items = []
            receives_month = []
            last_total = total_month
            total_savings = all_total + last_total
            for d in dues:
                total_dues, items = total_dues_month(d, date_current, total_dues, items)

            for r in receives:
                total_receive, receives_month = total_receives_month(r, date_current, total_receive, receives_month)

            total_month = total_receive - total_dues
            all_total = total_savings + total_month

            total.append({
                "tot_dues": str(total_dues),
                "items": items,
                "receives": receives_month,
                "tot_receive": str(total_receive),
                "total_month": str(total_month),
                "all_total_month": str(total_savings)
            })
            
        return JsonResponse(data=total, status=status.HTTP_200_OK, safe=False)



