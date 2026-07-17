from django.contrib import admin
from .models import Category,Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']

    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','description','price','stock','image','is_active','created_at']

    list_filter = ['is_active','category','created_at']

    list_editable = ['price','stock','is_active']

    prepopulated_fields = {'slug':('title',)}

    search_fields = ['title','description']