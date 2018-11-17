frase=str(input("Digite uma frase: ")).strip().upper() ##deixa tudo maiusculo
palavras=frase.split() ##separa a frase em um vetor de palavras
junto="".join(palavras) ##junta as palavras 
inverso=""
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso==junto:
    print("Temos um palíndromo!")
else:
    print("A frase Digitada não é um palíndromo!")
