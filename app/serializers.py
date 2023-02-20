from rest_framework import serializers
from .models import Employe


class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = ('id','name','adress','phone')

class Employe_post_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = ('id','name','adress','phone')

