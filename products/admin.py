from django.contrib import admin
from .models import Category, Products, ProductCart, Cart, Client, Order, Invoice

admin.site.site_header = 'MyStore'
admin.site.index_title = 'MyStore Admin'
admin.site.site_title = 'MyStore'

class ProductInline(admin.StackedInline):
    model = Products
    extra = 0

class ProductCartInline(admin.StackedInline):
    model = ProductCart
    extra = 0

class InvoiceInline(admin.StackedInline):
    model = Invoice
    extra = 0

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone_number', 'address']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'paid', 'sended', 'closed']
    inlines = [InvoiceInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [ProductInline]

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'available']
    list_filter = ['category', 'available']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'total', 'done', 'products_q', 'date_created', 'payment_code']
    inlines = [ProductCartInline]

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'payment_method', 'amount_paid', 'created_at']
