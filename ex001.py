"""Exercício de python"""

PI = 3.1415

print("Selecione um polígono para calcular a área")
print("1 - triângulo")
print("2 - retângulo")
print("3 - quadrado")
print("4 - trapézio")
print("5 - losango")
print("6 - circulo")

while True:
    opcoes = int(input())
    if 1 <= opcoes <= 6:
        break

    print("digite um número de 1 a 6")

if opcoes == 1:
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    print("A área do triângulo é de", ((base * altura)/2), "metros quadrados")

elif opcoes == 2:
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    print("A área do retângulo é de", (base * altura), "metros quadrados")

elif opcoes == 3:
    lado = float(input("Lado: "))
    print("A área do quadrado é de", (lado ** 2), "metros quadrados")

elif opcoes == 4:
    b = float(input("Base Menor: "))
    B = float(input("Base Maior: "))
    altura = float(input("Altura: "))
    area = ((b + B) * altura) / 2
    print("A área do trapézio é de", area, "metros quadrados")

elif opcoes == 5:
    D = float(input("Diagonal Maior: "))
    d = float(input("Diagonal Menor: "))
    print("A área do losango é de", ((D*d)/2))

elif opcoes == 6:
    raio = float(input("Raio: "))
    print(f"A área da é de {(PI * raio ** 2):.2f} metro quadrados")

palavra = input("Insira alguma palavra\n\n")

tamanho = len(palavra)
metadeDaPalavra = int(tamanho / 2)

print("\nPalavra Completa:", palavra)
print(f"\nPrimeira metade: {palavra[0:metadeDaPalavra]}")
print(f"\nSegunda metade: {palavra[metadeDaPalavra:tamanho]}")
print(f"\nSegundo caractere até o fim: {palavra[2:tamanho]}")
print(f"\nPalavra Duplicada: {palavra * 2}")
print(f"\nPalavra Triplicada: {palavra * 3}")
print(f"\nPalavra Concatenada: {palavra} + MatheusSoares")
