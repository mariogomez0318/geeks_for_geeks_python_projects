import random
import math

lower = int(input("Ingresa el limite inferior: "))
upper = int(input("Ingresa el limite superior: "))
random_var = random.randrange(lower,upper)
chances = math.ceil(math.log(upper-lower+1, 2))
counter = 0

while counter < chances:
    counter += 1
    ans = int(input("Adivina: "))
    if ans == random_var:
        print("has adivinado el numero en ")
        break
    elif ans < random_var:
        print("quedaste abajo")
    else:
        print("quedaste arriba")


if counter >= chances:
    print("se te acabaron los intentos")
else:

    print(counter, " intentos")