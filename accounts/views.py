from django.shortcuts import render
from django.db.models.query_utils import Q
from .models import Account

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class check_user(APIView):
    def get(self,request,user):
        data ={}
        try:
            if Account.objects.filter(Q(username=user)|Q(email=user)).exists() == True:
                account = Account.objects.get(Q(username=user)|Q(email=user))
                result = True
                data["username"]     = account.username
                data["email"]     = account.email
            else:
                result = False
            data["result"]     = result
        except:
            data["Error"]     = "Sorry something when wrong"
        return Response(data=data)
