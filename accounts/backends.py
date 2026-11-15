from django.contrib.auth.backends import BaseBackend

from accounts.models import UserModel

class EmailBackend(BaseBackend):

    def authenticate(self, request, username = None, password = None, **kwargs):

        try:

            user_object = UserModel.objects.get(email=username)

            if user_object.check_password(password):

                return user_object

        except:

            return None    

class PhoneBackend(BaseBackend):

    def authenticate(self, request, username = None, password = None, **kwargs):

        try:

            user_object = UserModel.objects.get(phone = username)

            if user_object:

                user_object.check_password(password)

                return user_object

        except:

            return None        