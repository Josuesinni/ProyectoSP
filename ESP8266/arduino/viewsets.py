from rest_framework import viewsets
from arduino.models import Arduino, Cliente, Entrada, Salida
from arduino.serializers import ArduinoSerializer, ClienteSerializer, EntradaSerializer, SalidaSerializer

class ArduinoViewSet(viewsets.ModelViewSet):
    queryset = Arduino.objects.all()
    serializer_class = ArduinoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

class SalidaViewSet(viewsets.ModelViewSet):
    queryset = Salida.objects.all()
    serializer_class = SalidaSerializer