from rest_framework import serializers
from .models import Kategori, UMKM, Produk

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class UMKMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UMKM
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'
