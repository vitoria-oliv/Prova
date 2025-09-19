from django.shortcuts import render
from .models import Tarefa

def listar_tarefas(request):
    # 1. a busca no banco de dados continua a mesma
    tarefas_salvas = Tarefa.objects.all()

    # 2. criamos um "dicionario do contexto" para enviar os dados ao template.
    # A chave 'minhas_tarefas' será a variável que usaremos no html.
    contexto = {
        'minhas_tarefas': tarefas_salvas 
    }

    # 3. renderizamos o tamplate, passando a requisição e o contexto com os dados.
    return render(request, 'tarefas/lista.html', contexto)