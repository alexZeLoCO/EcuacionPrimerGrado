print("La ecuación es del estilo: ax+b=0")      #GUIA PARA USUARIO

a = float (input ("Introduzca el valor de a: "))        #SOLICITA VALOR DE A
b = float (input ("Introduzca el valor de b: "))        #SOLICITA VALOR DE B

if (a==0 and b==0):     #SI A Y B SON 0 EL VALOR DE X NO IMPORTA
    print ("La ecuación se cumple para cualquier valor de x")       #OUTPUT
elif (a==0 and not b==0):       #SI A ES 0 PERO B NO ES 0. NINGÚN VALOR DE X CUMPLE
    print ("La ecuación no tiene solución.")        #OUTPUT
else:       #EL RESTO DE CASOS
    x = -b/a        #OPERACIÓN
    print ("El resultado es",x)     #OUTPUT