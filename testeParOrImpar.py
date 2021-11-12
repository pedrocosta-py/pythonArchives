valor = int(input("--> digite um numero par:"))
while (valor%2==0):
    try:
        number = int(input("--> digite um valor:"))

        if(number%2==0):
            print("this number is par")
        else:
            print("this number is impar")

    except:
        print("--> digite apenas numeros")

