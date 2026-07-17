from django.db import models
from django.db.models import CharField
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    # Category Name
    name = models.CharField(max_length=100,verbose_name="Kategori Adı")
    slug = models.SlugField(max_length=50,unique=True,blank=True,verbose_name="Slug")

    class Meta:
        verbose_name_plural = "Kategoriler"

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

class Product(models.Model):
    # Category Connection ---> One to Many
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')

    # Product Information
    title = models.CharField(max_length=100,verbose_name="Ürün Adı")
    description = models.TextField(verbose_name="Ürün Açıklaması")
    image = models.ImageField(upload_to='products/',blank=True,null=True,verbose_name="Ürün Resmi")
    slug = models.SlugField(max_length=50,unique=True,blank=True,verbose_name="Slug")

    # Price Information
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Ürün Fiyatı")
    stock = models.PositiveIntegerField(default=5,verbose_name="Stok Miktarı")

    # Status Information
    is_active = models.BooleanField(default=True,verbose_name="Ürün Durumu")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Ürün Oluşturma Tarihi")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Ürün Güncellenme Tarihi")

    class Meta:
        verbose_name_plural = "Ürünler"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)