termo = int(input("Quantos termos vc quer mostrar? "))
fibo1 = 0
fibo2 = 1
print("{} -> {}".format(fibo1,fibo2),end=" -> ")
contador = 3
while contador <= termo:
    print("{}".format(fibonnaci),end=" -> ")
    fibonnaci = fibo1 + fibo2
    fibo1 , fibo2 = fibo2,fibonnaci
    contador += 1
print("Fim")