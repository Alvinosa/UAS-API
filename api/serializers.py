from rest_framework import serializers
from .models import Kategori, UMKM, Produk

class KategoriSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Kategori
        fields = ['id', 'nama']

class UMKMSerializer(serializers.ModelSerializer):
    Kategori = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UMKM
        fields = ['id', 'Kategori', 'nama', 'alamat']

class ProdukSerializer(serializers.ModelSerializer):
    UMKM = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Produk
        fields = ['id', 'UMKM', 'UMKM', 'nama', 'harga', 'deskripsi']


