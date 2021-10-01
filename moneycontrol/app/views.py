from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Despesas
from .forms import DespesasForm

def index(request):
    return render(request, 'base.html')

# CRUD DESPESAS
def visualizarDespesas(request):
    despesas = Despesas.objects.all()
    return render(request, 'tabela_despesas.html',{'despesas':despesas})

def criarDespesas(request):
    form = DespesasForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_despesas')

    return render(request,'form_despesa.html', {'form':form})

def atualizarDespesas(request, id):
    despesas = Despesas.objects.get(id=id)
    form = DespesasForm(request.POST or None, instance=despesas)

    if form.is_valid():
        form.save()
        return redirect('lista_despesas')

    return render(request, 'form_despesa.html', {'form':form,'despesas':despesas})

def excluirDespesas(request, id):
    despesas = Despesas.objects.get(id=id)

    if request.method == 'POST':
        despesas.delete()
        return redirect('lista_despesas')

    return render(request, 'confirmar_remocao.html',{'parametro':despesas})
    
# CRUD PRODUTOS

