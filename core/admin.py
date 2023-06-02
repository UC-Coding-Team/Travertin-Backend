from django.contrib import admin
from django.utils.html import format_html

from core.models import Category, Product, Discount
from core.models.outsite import Navbartex


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    exclude = ('created_at', 'updated_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image_preview')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('image_preview',)
    exclude = ('created_at', 'updated_at')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" alt="Product Image">', obj.image.url)
        return 'No Image'

    image_preview.short_description = 'Image Preview'


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'display_image')
    list_filter = ('created_at',)
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Discount Information', {
            'fields': ('title', 'text', 'image', 'url')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return format_html('<span style="color: red;">(No image)</span>')

    display_image.short_description = 'Image'



@admin.register(Navbartex)
class NavbartexAdmin(admin.ModelAdmin):
    list_display = ('text', 'display_status', 'start_time', 'end_time')
    list_filter = ('status',)
    search_fields = ('text',)


    def display_status(self, obj):
        if obj.status == 'green':
            return format_html('<span style="color: green;">&#x25CF;</span>')
        elif obj.status == 'red':
            return format_html('<span style="color: red;">&#x25CF;</span>')
        return ''

    display_status.short_description = 'Status'

    def save_model(self, request, obj, form, change):
        # Customize the logic for saving the model here
        obj.save()