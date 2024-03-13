from rest_framework import serializers
from .models import Cliente

class ClienteSerializar(serializers.ModelSerializer):
    class Meta:
        model = Cliente 
        fields = ['id','nome','cidade']
    