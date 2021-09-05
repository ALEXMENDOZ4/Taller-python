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


def punto7(saldo):
    r = saldo + (saldo * 0.015)
    return print("el resultado es de: ", r) 

punto7(35000)


def punto8(sueldo):
    ley = sueldo * 0.01
    segurosocial = sueldo * 0.04
    seguroforsozo = sueldo * 0.005
    caja = sueldo * 0.05
    sueldo_final = sueldo - ley - segurosocial - seguroforsozo - caja

    return print("resultado de ley: ", ley, "resultado seguro social: ", segurosocial, "resultado seguro forsozo: ", seguroforsozo, "resultado caja:", caja, "resultado sueldo final: ", sueldo_final)

punto8(750000)



def punto9(n_palabras, tam, col):
    r = (n_palabras * 20000) + (tam * 15000) + (col * 25000)
    return print("el resultado es de: ", r) 

punto9(10,8,6)



def punto10(tiempo):
    r = 100000 + (120000 * (tiempo - 1))
    return print("el resultado es de: ", r) 

punto10(30)



def punto11(tiempo_horas):
    descuento = (tiempo_horas * 20000) * 0.05
    pago = tiempo_horas * 20000 - descuento
    return print("el resultado del pago", pago, "el resultado del descuento ", descuento)

punto11(5)



def punto12(inicial, final):
    r = (inicial - final) - ((inicial - final) * 0.2)
    return print("el resultado es de: ", r)

punto12(5,10)



def punto13(n_fotos):
    r = (n_fotos * 1500) + ((n_fotos * 1500) * 0.16)
    return print("el resultado es de: ", r)

punto13(15)



def punto14(monto):
    ginecologia =  monto * 0.4
    traumatologia = monto * 0.3
    pediatria = monto * 0.3

    return print("ginecologia: ", ginecologia,"traumatologia: ", traumatologia,"pediatria: ", pediatria)

punto14(150000)




def punto15(n_peliculas, n_dias):
    r = ((n_peliculas - 1) * 1500) * n_dias
    return print("el resultado es de: ", r)

punto15(10,15)



def punto16(n_personas, n_dias):
    total = (n_personas * 25000) * n_dias
    total_iva = total + total * 0.12
    r = total_iva
    return print("el resultado es de: ", r)

punto16(10,8)

