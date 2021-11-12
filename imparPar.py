"""
Created by sudoAptIPedro
    
"""
def numberParImpar():
    valor = int(input("--> digite um numero par:"))
    while (valor%2==0):
        try:
            number = int(input("--> digite um valor:"))

            if(number%2==0):
                print("Numero par!")
            else:
                print("Numero impar!")

        except:
            print("--> digite apenas numeros")       

#    
#
inicio = str(input('--> Deseja iniciar? \n --> yes(y) or no(n) \n -->'))
#
if(inicio == 'y'):
    numberParImpar()
else:
    print("--> P R O G R A M A  E N C E R R A D O")
