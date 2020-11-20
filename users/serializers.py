from users.models import Sp_user
from rest_framework import serializers


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sp_user
        fields = '__all__'
