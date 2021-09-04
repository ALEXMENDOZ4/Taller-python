def punto1():
    y = ( ( 5 + 2 - 5)**2 * 5 + 8 / 2 - 30) / 2 * 5 - 3
    return print ("el resultado es de: ", int(y))

punto1()


def punto2():
    z = 5
    n = 3
    m = z - n
    y = (((z + 2 - n)**2 * m + 8 / 2 - 30) / 2 * 5 - 3 )**5 + 15 * 3 - 9 / 3
    return print("el resultado es de: ", y)

punto2()


def punto3():
    z = 5
    n = ((8+2-4)**2 * 5 + 8 + 7 / 2 - 30* 5 ) / 2 * 5 - 3;
    m = z**2 * 3 + n;
    y = ((((z+2-n)**2 * m+8/2 - 30) / 2 * 5 - 3)**5 + 15 * 3 - 9 / 3)**2 - 5 / 4
    return print("el resultado es de: ", y)

punto3()


def punto4(p, v, t):
    r =(p * v) / (0.37 * (t + 460))
    return print("el resultado es de: ", r)

punto4(4,10,15)


def punto5(edad):
    r = (200 - edad) / 10
    return print("el resultado es de: ", r) 

punto5(10)


def punto6(inv1, inv2, inv3):
    total = inv1 + inv2 + inv3
    porcentaje1 = inv1 * 100 / total
    porcentaje2 = inv2 * 100 / total
    porcentaje3 = inv3 * 100 / total
    return print("resultado: ", porcentaje1,"resultado: ", porcentaje2,"resultado: ", porcentaje3)

punto6(1000,2000,3000)