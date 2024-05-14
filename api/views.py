from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Kategori, UMKM, Produk
from .serializers import KategoriSerializer, UMKMSerializer, ProdukSerializer
from rest_framework.views import APIView

class KategoriListCreate(generics.ListCreateAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

    def delete(self, request, *args, **kwargs):
        Kategori.object.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UMKMListCreate(generics.ListCreateAPIView):
    queryset = UMKM.objects.all()
    serializer_class = UMKMSerializer

    def delete(self, request, *args, **kwargs):
        UMKM.object.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProdukListCreate(generics.ListCreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

    def delete(self, request, *args, **kwargs):
       Produk.object.all().delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
    
class KategoriList(APIView):
    def get(self, request, format=None):
        Kategori = Kategori.objects.all()
        serializer = KategoriSerializer(Kategori, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = KategoriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erorrs, status=status.HTTP_400_BAD_REQUEST)
    
class UMKMList(APIView):
    def get(self, request, format=None):
        UMKM = UMKM.objects.all()
        serializer = UMKMSerializer(UMKM, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UMKMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erorrs, status=status.HTTP_400_BAD_REQUEST)
    
class ProdukList(APIView):
    def get(self, request, format=None):
        Produk = Produk.objects.all()
        serializer = ProdukSerializer(Produk, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProdukSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erorrs, status=status.HTTP_400_BAD_REQUEST)
