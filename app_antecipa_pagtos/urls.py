from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ModeloView, PaginaInicialView, AdministradorView
from .views import FornecedoresCreate, ParcelasCreate, LogsCreate
from .views import FornecedoresUpdate, ParcelasUpdate, LogsUpdate
from .views import FornecedoresDelete, ParcelasDelete, LogsDelete
from .views import FornecedoresList, ParcelasList, LogsList

urlpatterns = [
    path('', ModeloView.as_view(), name='modelo'),
    path('inicio', PaginaInicialView.as_view(), name='inicio'),
    path('admin', AdministradorView.as_view(), name='admin'),
    path('fornecedores', FornecedoresCreate.as_view(), name='fornecedores'),
    path('parcelas', ParcelasCreate.as_view(), name='parcelas'),
    path('logs', LogsCreate.as_view(), name='logs'),

    path('editar-fornecedores/<int:pk>/', FornecedoresUpdate.as_view(), name='editar-fornecedores/'),
    path('editar-parcelas/<int:pk>/', ParcelasUpdate.as_view(), name='editar-parcelas/'),
    path('editar-logs/<int:pk>/', LogsUpdate.as_view(), name='editar-logs/'),

    path('deletar-fornecedores/<int:pk>/', FornecedoresDelete.as_view(), name='deletar-fornecedores/'),
    path('deletar-parcelas/<int:pk>/', ParcelasDelete.as_view(), name='deletar-parcelas/'),
    path('deletar-logs/<int:pk>/', LogsDelete.as_view(), name='deletar-logs/'),

    path('listar-fornecedores/', FornecedoresList.as_view(), name='listar-fornecedores/'),
    path('listar-parcelas/', ParcelasList.as_view(), name='listar-parcelas/'),
    path('listar-logs/', LogsList.as_view(), name='listar-logs/'),

    path('login', auth_views.LoginView.as_view(
          template_name='login.html'
         ), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]