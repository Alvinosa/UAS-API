from django.db import models

class Kategori(models.Model):

    nama = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nama

class UMKM(models.Model):
    Kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='umkm')
    nama = models.CharField(max_length=100)
    alamat = models.TextField()

    def __str__(self):
        return self.Kategori

class Produk(models.Model):
    UMKM = models.ForeignKey(UMKM, on_delete=models.CASCADE, related_name='umkm')
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField()

    def __str__(self):
        return self.UMKM
    
    name = models.CharField(max_length=100)
    address = models.TextField()

class UMKM(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    vendor = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='umkm')

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField()
    food = models.ForeignKey(UMKM, on_delete=models.CASCADE, related_name='produk')
    user = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='produk')
    comment = models.TextField()

   

