from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('despesas', views.visualizarDespesas, name="lista_despesas"),
    path('criar/despesas', views.criarDespesas, name="criar_despesas"),
    path('atualizar/despesas/<int:id>/', views.atualizarDespesas, name="atualizar_despesas"),
    path('excluir/despesas/<int:id>/', views.excluirDespesas, name="excluir_despesas"),

    path('produtos', views.visualizarDespesas, name="lista_produtos"),
    path('criar/produtos', views.criarDespesas, name="criar_produtos"),

    path('prestadores', views.visualizarDespesas, name="lista_prestadores"),
    path('criar/prestadores', views.criarDespesas, name="criar_prestadores"),

    path('funcionarios', views.visualizarDespesas, name="lista_funcionarios"),
    path('criar/funcionarios', views.criarDespesas, name="criar_funcionarios"),
]
