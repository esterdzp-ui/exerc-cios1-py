#Entrada:pedir o nome do jogador
nome = input("Digite o nome do jogador:")

#Entrada:pediro nivel atual
nivel_atual = int(input("Digite o nível atual do jogador:"))

#Processamento:calcular o próximo nível 
proximo_nivel = nivel_atual + 1

#saída:mostrar a mensagem
print(f"Parabéns{nome}, seu próximo objetivo é o nível{proximo_nivel}!")
