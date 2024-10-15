resultado: int
def suma_dos_valores(sumando1,sumando2):
    global resultado
    resultado=sumando1 + sumando2
    return resultado 

#suma_dos_valores(4,5)
#print("primera suma")
#print (resultado)
#suma_dos_valores(1,2)
#print("segunda suma")
#print(resultado)

def calculadora_dos_valores(numero1, numero2, operador):
    global resultado
    if operador ==1: #si el operador es 1 es suma
        resultado=numero1 + numero2
        return resultado
    elif operador ==2: #si el operador es 2 es resta
        resultado = numero1 - numero2
        return resultado
    elif operador ==3: #si el operador es 3 es mult
       resultado = numero1 * numero2
       return resultado
    elif operador ==4: #si el operador es 4 es division
      resultado = numero1 / numero2
      return resultado
    else: # si el operador es otro numero 
        print("el numero ingresado no es valido")
        return resultado 
    
#calculadora_dos_valores(1,2,1)
#print ("suma:", resultado)
#calculadora_dos_valores(10,5,2)
#print ("resta:", resultado)
#calculadora_dos_valores(4,5,3)
#print ("multiplicacion:", resultado)
#calculadora_dos_valores(7,6,4)
#print ("division:", resultado)

#def pitagoras(a,b):
    global c
    c=(a**2+b**2)**0.5
    return c

#pitagoras(3,4)
#print ("pitagoras",c)

#def despeje_x():
    b=int(input("ingrese el valor de b= "))
    c=int(input("ingrese el valor de c= "))
    x=(c-b)/2
    print("el valor de x es: ",x)
    return x

#despeje_x ()

#def calcular_valores():

    global resultados
    a=bool(input("ingresa el valor de a= "))
    b=bool(input("ingresa el valor de b= "))
    c=bool(input("ingresa el valor de c= "))
    x=(a and b and c)
    print ("el valor de x: ", x)
    return x

#calcular_valores()

#def pitagoras_funcion_sumar():
    global result_pitagoras
    a=int(input("ingresar el valor de a= "))
    b=int(input("ingresar el valor de b= "))
    a2= a**2
    b2= a**2
    suma= suma_dos_valores(a2,b2)
    resul_pitagoras= suma**0.5
    print("el valor de pitagora es:", resul_pitagoras)
    return resul_pitagoras

#pitagoras_funcion_sumar()

#def contador
#global resultado_contador
#palabra=str(input("ingrese la pablabra a contar letras: "))
#letra=str(input("ingrese a letra a contar: "))
#resultado_contador =palabra.com (letras)



#def compa_contador():
    global resultado_compa_contador
    palabras= str(input("ingresar palabras que se mostraran"))
    letra=str(input("ingresar letras"))
    resultado_contador =palabras.count(letra)
    print("la cantidad de letras",letra, "es= ", resultado_contador)
    print("la cantidad de letras de la palabras es=", len(palabras))
    print("palabras separada por letras=",list(palabras))
#compa_contador()


 
