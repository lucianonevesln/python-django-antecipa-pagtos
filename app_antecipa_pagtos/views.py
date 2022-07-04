from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Fornecedores, Parcelas, Logs
from django.urls import reverse_lazy


#################### Base Views ####################


class ModeloView(TemplateView):
    template_name = 'modelo.html'


class PaginaInicialView(TemplateView):
    template_name = 'inicio.html'


class AdministradorView(TemplateView):
    template_name = 'admin'


#################### Create ####################


class FornecedoresCreate(CreateView):
    model = Fornecedores
    fields = '__all__'
    template_name = 'form_fornecedores.html'
    success_url = reverse_lazy('parcelas')


class ParcelasCreate(CreateView):
    model = Parcelas
    fields = ['id_fornecedor', 'data_emissao', 'data_vencimento', 'valor_original']
    template_name = 'form_parcelas.html'
    success_url = reverse_lazy('logs')


class LogsCreate(CreateView):
    model = Logs
    fields = '__all__'
    template_name = 'form_logs.html'
    success_url = reverse_lazy('inicio')


#################### Update ####################


class FornecedoresUpdate(UpdateView):
    model = Fornecedores
    fields = '__all__'
    template_name = 'form_fornecedores.html'
    success_url = reverse_lazy('parcelas')


class ParcelasUpdate(UpdateView):
    model = Parcelas
    fields = ['id_fornecedor', 'data_vencimento_nova', 'data_vencimento']
    template_name = 'form_parcelas.html'
    success_url = reverse_lazy('logs')


class LogsUpdate(UpdateView):
    model = Logs
    fields = '__all__'
    template_name = 'form_logs.html'
    success_url = reverse_lazy('inicio')


#################### Delete ####################


class FornecedoresDelete(DeleteView):
    model = Fornecedores
    template_name = 'deletar_fornecedores.html'
    success_url = reverse_lazy('parcelas')


class ParcelasDelete(DeleteView):
    model = Parcelas
    template_name = 'deletar_parcelas.html'
    success_url = reverse_lazy('logs')


class LogsDelete(DeleteView):
    model = Logs
    template_name = 'deletar_logs.html'
    success_url = reverse_lazy('inicio')


#################### ListView ####################


class FornecedoresList(ListView):
    model = Fornecedores
    template_name = 'listar_fornecedores.html'


class ParcelasList(ListView):
    model = Parcelas
    template_name = 'listar_parcelas.html'


class LogsList(ListView):
    model = Logs
    template_name = 'listar_logs.html'