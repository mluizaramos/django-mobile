from django.shortcuts import render
from .models import Cliente
from .serializer import ClienteSerializar
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework import status


@api_view(['GET','POST'])
def listar_clientes(request):
    if request.method == 'GET':
        queryset = Cliente.objects.all()
        serializer = ClienteSerializar(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClienteSerializar(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientesView(ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializar
    