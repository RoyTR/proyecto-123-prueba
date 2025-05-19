#Un banco establece que la clave secreta para acceso
#a sus cajeros automáticos debe ser un número de cuatro
#o más dígitos y que la suma de los dos dígitos que se encuentran
#en la 3 y 4 posición (posición de centena y millar) sea par.
#Determinar si una clave cumple con la condición.

#def nombre_metodo(varaibles que recibe (opciones)):

#saber si es 4 digitos
def clave_ingresada_es_4_digitos(clave):
    if len(clave) == 4:
        print("SI es de 4 digitos")
    else:
        print("NO es de 4 digitos")

#posicion 3 + posicion 4 es par

#si cumple las 2, entonces es clave correcta



clave_ingresada = input("Ingrese la clave: ")

print(f"La clave ingresada es: {clave_ingresada}")

clave_ingresada_es_4_digitos(clave_ingresada)
