#num1 = int(input("digite seu número:"))
#num2 = int(input("digite seu número:"))
#operacao = (input("digite o tipo de operação:"))
#match operacao:
    #case "+":
       # soma = num1 + num2
        #print("soma" , soma)

   # case "/":
       # divisao = num1 / num2 
       # print("divisao" , divisao)

   # case "-":
        #subtracao = num1 - num2
        #print("Subtração:", subtracao)

    #case "*":
        #multiplicacao = num1 * num2
        #print("Multiplicação:", multiplicacao)

#idade = int(input("Digite sua idade: "))
#match idade:
    #case x if x > 12 and x < 18:
      #  print("")
       # idade = int(input("Digite sua idade: "))
    #case x if x < 18:
     #   print("Adolescente" )
    #case x if x < 60:
      #  print("Adulto")
    #case x if x < 100:
     #   print("Idoso")
    #case x if x >= 100:
     #   print("Múmia")
    #case _:
     #   print("Idade inválida")



nota = int(input("Digite sua nota: "))
match nota:
    case "10":
        print("Parabéns, fez mais que sua obrigação")
    case 9 | 8 | 7:
        print("Aprovado, mas deve estar mais joema do calypso ")
    case 6 | 5 | 4 | 3 | 2 | 1 | 0:
        print("Reprovado, estudar mais da proxima vez jumento")
    case _:
         print("Nota inválida")