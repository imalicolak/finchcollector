from django.contrib import admin
from .models import Guitar, Updates, Upgrade

# Register your models here.

admin.site.register(Guitar)
admin.site.register(Updates)
admin.site.register(Upgrade)
