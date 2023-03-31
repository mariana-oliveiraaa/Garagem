from django.contrib import admin

from .models import Acessorio, Cor, Marca, Categoria, Veiculo

admin.site.register(Acessorio)
admin.site.register(Cor)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Veiculo)