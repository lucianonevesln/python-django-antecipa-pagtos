from django.contrib import admin
from .models import Fornecedores, Logs, Parcelas

# Register your models here.
admin.site.register(Fornecedores)
admin.site.register(Logs)
admin.site.register(Parcelas)