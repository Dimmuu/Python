def fatorial(numero):
    if(numero==0 or numero==1):
        return 1
    else:
        return numero* fatorial(numero-1)

x=int(input("Digite um número para calcular seu fatorial:"))
print("O fatorial de %d é %d"%(x,fatorial(x)))
