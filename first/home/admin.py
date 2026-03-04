from django.contrib import admin

# Register your models here.
from .models import Home

# admin.site.register(Home)

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Home, HomeAdmin)