from django.contrib import admin

# Register your models here.

from django.contrib import admin


from product.models import Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
