import random

words = ['avion', 'carro', 'grua', 'balon', 'envoltura', 'gato', 'carro', 
        'zanahoria']
rword = random.choice(words)
intentos = 3
almacen = ''
while intentos > 0:
    fcount = 0
    for i in rword:
        if i in almacen:
            print(i)
        else:
            print("_")
            fcount += 1
    if fcount == 0:
        print("lo has completado: ", rword)
        break
    intento = input("ingresa una letra: ")
    almacen += intento

    if intento not in rword:
        intentos -= 1
        print("mal, has perdido un intento, te quedan: ", intentos, "intentos")
    if intentos == 0:
        print("se te acabaron los intentos, perdiste")


    

        
    
    



