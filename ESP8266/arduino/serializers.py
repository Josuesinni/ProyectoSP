from rest_framework import serializers

from arduino.models import Arduino, Cliente, Entrada, Salida
class ArduinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arduino
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = '__all__'

class SalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salida
        fields = '__all__'