from django.contrib import admin
from Restaurant.models import Restaurant, Menu

class MenuInline(admin.TabularInline):
    model = Menu
    extra = 3

class RestaurantAdmin(admin.ModelAdmin):
    fields = ['name','description']
    inlines = [MenuInline]




admin.site.register(Restaurant, RestaurantAdmin)
