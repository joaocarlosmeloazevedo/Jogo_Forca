from random import randint

print("Bem vindo ao jogo da forca!")

menu = int
palavras = ["EMPURRE", "ARQUEOLOGIA", "ESPAGUETE", "JARDIM", "ASTRONAUTA", "CINTURA", "SEMEADURA", "UTILIDADE", "LIVRO", "CICRATIZAÇAO"]

def sortear_palavra(palavras):
        i = randint(0, (len(palavras) - 1))
        print(palavras[i])

        

while menu != 2:
         menu = int(input("Para jogar digite: 1\nPara sair digite: 2\n"))

         if menu == 1:
             sortear_palavra(palavras)

exit()
            
     

