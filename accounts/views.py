from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

from accounts.serailzier import UserSerailizer
from accounts.models import UserModel


class UserRegisterView(APIView):

    def post(self,request):

        form_data= request.data

        serilaizer_instance = UserSerailizer(data=form_data)

        if serilaizer_instance.is_valid():

            cleaned_data= serilaizer_instance.validated_data

            qs = UserModel.objects.create_user(**cleaned_data)

            serilaizer_instance = UserSerailizer(qs)

            return Response(data=serilaizer_instance.data)

        else:return Response(data=serilaizer_instance.errors)


class GetMeView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

     user = request.user

     instance = get_object_or_404(UserModel,username=user)

     serializer = UserSerailizer(instance)

     return Response(data=serializer.data)