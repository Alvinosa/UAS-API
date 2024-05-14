from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('Kategori/', views.KategoriListCreate.as_view(),name="Kategori-view-create"),
    path('api/Kategori/', views.KategoriList.as_view()),
    path('UMKM/', views.UMKMListCreate.as_view(),name="UMKM-view-create"),
    path('api/UMKM/', views.UMKMList.as_view()),
    path('Produk/', views.ProdukListCreate.as_view(),name="Produk-view-create"),
    path('api/Produk/', views.ProdukList.as_view()),
]