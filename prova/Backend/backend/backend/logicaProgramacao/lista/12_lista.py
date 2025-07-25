# Lista inicial de tarefas 

minhas_tarefas = [" Levar o cachorro para passear" , "Ir na vizinha conversar" , "Varrer a calçada" , "Comprar pão" , "Ver o jacaré no lago"]
print(f"Tarefaz pendentes: {minhas_tarefas}")

# Adicionando uma nova tarefa ao final da lista

minhas_tarefas.append("Ler um livro")
print(f"Tarefa adicionada: {minhas_tarefas}")

# Adicionando uma tarefa em posição específica (indice 3)

minhas_tarefas.insert(3, "Ir na vó almoçar")
print(f"Tarefa inserida em posição específica: {minhas_tarefas}")

#Removendo uma tarefa que já foi feita (pelo nome)

minhas_tarefas.remove("Comprar pão")
print(f"Tarefa 'Comprar pão' removida: {minhas_tarefas}")

# Removendo a última tarefa (útil pilhas)

tarefa_removida = minhas_tarefas.pop() # remove ler um livro
print(f" Última tarefa removida ('{tarefa_removida}'): {minhas_tarefas}")
