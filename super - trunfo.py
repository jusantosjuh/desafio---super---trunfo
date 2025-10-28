# Desafio Lógica Super Trunfo
# Feito por Júllia Pontes
# (se quiser pode colocar a data ou nome da faculdade)

cartas = {
    "Leão": {"força": 90, "velocidade": 70, "inteligência": 40},
    "Tigre": {"força": 85, "velocidade": 75, "inteligência": 50},
    "Elefante": {"força": 95, "velocidade": 40, "inteligência": 60},
    "Raposa": {"força": 50, "velocidade": 80, "inteligência": 90}
}

print("=== Jogo Super Trunfo ===")
print("Cartas disponíveis: ")
for nome in cartas.keys():
    print("-", nome)

jogador1 = input("\nJogador 1, escolha sua carta: ").capitalize()
jogador2 = input("Jogador 2, escolha sua carta: ").capitalize()

print(f"\nCarta de {jogador1}: {cartas[jogador1]}")
print(f"Carta de {jogador2}: {cartas[jogador2]}")

atributo = input("\nEscolha o atributo (força, velocidade ou inteligência): ").lower()

valor1 = cartas[jogador1][atributo]
valor2 = cartas[jogador2][atributo]

print(f"\n{jogador1} tem {valor1} de {atributo}")
print(f"{jogador2} tem {valor2} de {atributo}")

if valor1 > valor2:
    print(f"\n🏆 {jogador1} venceu!")
elif valor2 > valor1:
    print(f"\n🏆 {jogador2} venceu!")
else:
    print("\nEmpate!")
