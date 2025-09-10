# numeroCl1 = int(input("quantos clientes vc quer cadastrar?"))

# clientes = []

# clientes = [["Cleiton","Eslováquia","Wellingtom"], 
#             [23, 69, 12],
#             ["Shaw!", "guarana", "Ediro" ]]

# print(clientes[0][1])
# print(clientes[1][1])
# print(clientes[2][0])

# vetor = [0 for i in range(numeroCl1)]

# for i in range(numeroCl1):
#     clientes.insert(i, input("Nome do Cliente: "))

# print (clientes)

# clientes.pop(2)
# print(clientes)

# numeroCl1 = int(input("quantos clientes vc quer cadastrar?"))
# vetor = [0 for i in range(numeroCl1)]

# for i in range(numeroCl1):
#     print("\n digite os paranauê das pessoa ai {i}")
#     nome = input("nome: ")
#     idade = int(input("idade: "))
#     genero = input("genero: ")

#     vetor[i] = {
#         "nome": nome,
#         "idade": idade,
#         "genero": genero
#     }

# # print("\n lista de pessoas cadrastradas: ")
# # for pessoas in vetor:

# #     print(pessoas)
    
# print(vetor[1]["nome"])
# print(vetor[0]["nome"])

# print(vetor)

from random import randint

computador = randint(0, 5)

pontuacao = 0


opcaoj1 = int(input("que numero vc escolhe: "))


if computador == opcaoj1:
    print("Parabéns, você acertou, yeyy \n")
    pontuacao = pontuacao + 1

elif computador != opcaoj1:
    print(f"você explodiu, eu estava pensando em {computador}  \n")

jgdnv = int(input("Voce quer jogar de novo? \n 0 - jogar denovo \n 1 - continuar"))

while jgdnv == 1:
   from random import randint

   computador = randint(0, 5)

   opcaoj1 = int(input("que numero vc escolhe: "))


   if computador == opcaoj1:
       print("Parabéns, você acertou, yeyy \n")
       pontuacao = pontuacao + 1

   elif computador != opcaoj1:
       print(f"você explodiu, eu estava pensando em {computador}  \n")

   jgdnv = int(input("Voce quer jogar de novo? \n 0 - Parar \n 1 - continuar"))

   if jgdnv == 0:
       print(f"sua pontuação foi {pontuacao}, boa :)")