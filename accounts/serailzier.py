from rest_framework import serializers

from accounts.models import UserModel,UserProfileModel

class UserSerailizer(serializers.ModelSerializer):

    class Meta:

        model = UserModel

        fields = ["id","username","email","password","phone"]

        extra_kwargs = {

            "password":{"write_only":True}
        }

class ProfilSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserProfileModel

        fields = "__all__"

        read_only_fields = ["id","owner"]       