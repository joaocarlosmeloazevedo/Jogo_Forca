from random import randint

print("Bem vindo ao jogo da forca!")

menu = int
palavras = ["EMPURRE", "ARQUEOLOGIA", "ESPAGUETE", "JARDIM", "ASTRONAUTA", "CINTURA", "SEMEADURA", "UTILIDADE", "LIVRO", "CICRATIZAÇAO"]


def iniciar_jogo(palavras):
        letra_resp = []
        letras_usadas = []
        i = randint(0, (len(palavras) - 1))
        resposta = palavras[i]
        print(resposta)
        acertou_palpite = False
        erros = 0

        for i in resposta:
                letra_resp.append(i)
        
        print("A palavra é:", len(resposta) * "_ ")
        while acertou_palpite == False or erros == 6:
                
                palpite = input("Digite uma letra ou uma palavra: ").upper()

                if palpite in letra_resp and palpite not in letras_usadas:
                        print("kkkk")
                        letras_usadas.append(palpite)

                elif palpite == resposta:
                        acertou_palpite = True
                        print("A RESPOSTA ERA ", resposta, "! ! !\n Parabéns!!!\n Nº de erros: ", erros)
                
                elif palpite in letras_usadas:
                        print("Você ja usou essa letra.\nLetras usadas: ")
                        for letras in letras_usadas:
                                print(letras)
                
                else:
                        print("Essa letra não existe nesta palavra kkkkk")
                        letras_usadas.append(palpite)
                        erros += 1
                        
while menu != 2:
         menu = int(input("Para jogar digite: 1\nPara sair digite: 2\n"))

         if menu == 1:
             iniciar_jogo(palavras)

exit()
            
     

