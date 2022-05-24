opcoes = 0
while(opcoes < 1 or opcoes > 6):
    print("Selecione um para calcular")
    print("1 - triângulo")
    print("2 - retângulo")
    print("3 - quadrado")
    print("4 - trapézio")
    print("5 - losango")
    print("6 - circulo")
    opcoes = int(input("\n"))

if (opcoes == 1):
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    print("A área do triângulo é de", ((base * altura)/2), "metros quadrados")

elif (opcoes == 2):
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    print("A área do retângulo é de", (base * altura), "metros quadrados")

elif (opcoes == 3):
    lado = float(input("Lado: "))
    print("A área do quadrado é de", (lado ** 2), "metros quadrados")

elif (opcoes == 4):
    b = float(input("Base Menor: "))
    B = float(input("Base Maior: "))
    altura = float(input("Altura: "))
    area = ((b + B) * altura) / 2
    print("A área do trapézio é de", area, "metros quadrados")

elif (opcoes == 5):
    D = float(input("Diagonal Maior: "))
    d = float(input("Diagonal Menor: "))
    print("A área do losango é de", ((D*d)/2))

elif (opcoes == 6):
    pi = 3.1415
    raio = float(input("Raio: "))
    print("A área da circunferência é de {:.2f} metros quadrados".format((pi*(raio**2))))



# -------------------------------------------------------------------------


palavra = input("Insira alguma palavra\n\n")

tamanho = len(palavra)
metadeDaPalavra = int(tamanho / 2)

print("\nPalavra Completa:",palavra)
print("\nPrimeira metade: {}".format(palavra[0:metadeDaPalavra]))
print("\nSegunda metade: {}".format(palavra[metadeDaPalavra:tamanho]))
print("\nSegundo caractere até o fim: {}".format(palavra[2:tamanho]))
print("\nPalavra Duplicada: {}".format(palavra*2))
print("\nPalavra Triplicada: {}".format(palavra*3))
print("\nPalavra Concatenada: {}".format(palavra+"MatheusSoares"))