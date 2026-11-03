from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

from leads.models import Lead
from leads.serailzers import LeadSerailizer
from leads.permission import IsOwner


class LeadsListCreateView(ListCreateAPIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = LeadSerailizer

    queryset = Lead.objects.all()

    def perform_create(self,serializer):

       serializer.save(created_by=self.request.user)

class LeadsRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsOwner]

    serializer_class = LeadSerailizer

    queryset = Lead.objects.all()       