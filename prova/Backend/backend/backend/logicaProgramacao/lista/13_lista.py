# Lista dos sonhos

lista = []
print(f"Lista inicial: {lista}")
Lista_sonhos = ["Viajar o mundo" , "Apreender a fazer comida" , " visitar a fonte dos  desehos em roma" , "Pular de paraquedas" ,  " Fazer uma trillha a cavalo na argentina" , "Ver uma girafa de perto" , "visitar a Igreja de roma" , "Ir no show do Jorge e mateus" ]

# adicionar mais 2 itens na lista dos sonhos

Lista_sonhos.insert(3, "Andar em um elefante")
print(f"Sonho inserido em posição específica: {Lista_sonhos}")

Lista_sonhos.insert(4, "ver barretos")
print(f"Sonho inserido em posição específica: {Lista_sonhos}")

# remover o sonho de uma posiçaõ específica
del Lista_sonhos[5]

Lista_sonhos.remove("Ver uma girafa de perto")
print(f"sonho 'Ver uma girafa de perto' removida: {Lista_sonhos}")

# remover o último sonho 

sonho_removido = Lista_sonhos.pop() 
print(f"Último sonho removido ('{sonho_removido}'): {Lista_sonhos}")
