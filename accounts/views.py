from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

from accounts.serailzier import UserSerailizer,ProfilSerializer
from accounts.models import UserModel
from accounts.models import UserProfileModel

from leads.permission import IsOwner


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


class UpdateProfileView(APIView):

   authentication_classes = [JWTAuthentication]

   permission_classes = [permissions.IsAuthenticated,IsOwner]

   def put(self,request):

      form_data = request.data

      profile_object = UserProfileModel.objects.get(owner=request.user)

      serializer = ProfilSerializer(data=form_data,instance = profile_object)

      if serializer.is_valid():

         serializer.save()

         return Response(data=serializer.data)

      else:return Response(data=serializer.errors)


class GetMeView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

     user = request.user

     instance = get_object_or_404(UserProfileModel,owner=user)

     serializer = ProfilSerializer(instance)

     return Response(data=serializer.data)


    