y = int(input('Digite um valor qualquer: '))

if y == 0:
    print("ERRO: Digite um valor acima de 0.")
elif y % 2 == 0:
    print("Este valor é par")
else:
    print("Este valor é ímpar")