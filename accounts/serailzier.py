from rest_framework import serializers

from accounts.models import UserModel

class UserSerailizer(serializers.ModelSerializer):

    class Meta:

        model = UserModel

        fields = ["id","username","email","password","phone"]