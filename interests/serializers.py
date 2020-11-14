from  rest_framework import serializers
from .models import Interest

class InterestSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class  Meta:
        model = Interest
        fields = ['id', 'name']