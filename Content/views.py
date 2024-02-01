from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from django.db import connection, transaction, connections
import sys, os, datetime, re , time,random,requests
from datetime import datetime
from django.core.mail import EmailMultiAlternatives


def Insert_q(data):
    with connections['LucknowGolfClub'].cursor() as cursor:
        resp = cursor.execute(""" Insert into RawPrac.OurSiteMember (first_name, last_name, phone, email, password) 
        values (%s,%s,%s,%s,%s) """, data)
        return resp
    
def List_q():
    with connections["LucknowGolfClub"].cursor() as cursor:
        resp = cursor.execute(f""" SELECT ID as KeyIndex,first_name, last_name, phone, email
        From RawPrac.OurSiteMember ; """)
        if resp and cursor.rowcount:
            resp = dictfetchall(cursor)
        else:
            resp = None
    return resp




def dictfetchall(cursor = ''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor = ''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))


def Home(request):
    current_datetime = datetime.now()
    time = current_datetime.strftime("%H:%M:%S")
    date=current_datetime.strftime("%Y-%m-%d")
    thoughts="Success usually comes to those who are too busy to be looking for it"
    data={}
    image="/media/weather1.png"
    data = [{'a':time,
             'b':date,
             'image':image,
             'Temp':'22',
             'thoughts':thoughts}]
    return render(request, 'Home.html', {'Data': data})


def About(request):
    
    return render(request, 'About.html')

def Index(request):
    
    return render(request, 'Index.html')

def Savedata(request):
    data=request.POST
    postdata=request.POST
    list=[]
    list.append(postdata.get('first_name'))
    list.append(postdata.get('last_name'))
    list.append(postdata.get('phone'))
    list.append(postdata.get('email'))
    list.append(postdata.get('password'))
    print(list)
    Insert_q(list)
    return render(request,'About.html')

def ShowData(request):
    data=List_q()
    return render(request, 'Show.html', {'members': data})







