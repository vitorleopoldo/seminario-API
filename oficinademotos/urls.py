"""oficinademotos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from clientes.views import clientesViewSet
from fornecedores.views import fornecedoresViewSet
from notafiscal.views import notafiscalViewSet
from produtos.views import produtosViewSet
from vendas.views import vendasViewSet
from funcionarios.views import funcionariosViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register (r'clientes', clientesViewSet) 
router.register (r'fornecedores', fornecedoresViewSet)
router.register (r'notafiscal', notafiscalViewSet)
router.register (r'produtos', produtosViewSet)
router.register (r'vendas', vendasViewSet)
router.register (r'funcionarios', funcionariosViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))

]
