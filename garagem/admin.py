from django.contrib import admin

from .models import Acessorio, Marca, Categoria

admin.site.register(Acessorio)
admin.site.register(Marca)
admin.site.register(Categoria)