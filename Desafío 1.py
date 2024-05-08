#1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

num = input('Ingrese un número de 3 dígitos: ')  #Inicializamos variable através del ingreso por teclado.

num_Invertido = int(str(num)[::-1]) #Convertimos el número en string y le invertimos el orden. Luego lo volvemos a convertir en Int. El resultado de ello es almacenado en una nueva variable.

print('El número en el orden inverso es: ',num_Invertido)   #Imprimimos en pantalla el resultado
