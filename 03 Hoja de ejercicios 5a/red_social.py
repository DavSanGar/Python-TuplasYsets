'''Una red social tiene una base de datos de usuarios y sus correspondientes amistades.

Crea un programa que tome una base de datos de una red social como una lista de
tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. 

Los nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas
diferentes. Deberas eliminar las cuentas duplicadas y después devolver una tupla de
tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.

Pista 1: Tus datos de entrada podrían ser así —> red_social = [("Juan", ["Maria", "Pedro",
"Luis"]), ("Maria", ["Juan", “Pedro”,”Juan”]), ("Pedro", ["Juan", "Maria"]), ("Luis", [“Juan”])]

Pista 2: Para eliminar duplicidades puedes usar sets
'''

red_social = [("Juan", ["Maria", "Pedro", "Luis"]), ("Maria", ["Juan", "Pedro", "Juan"]), 
("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]

#Eliminar las cuentas duplicadas en amigos
# for i in range(len(red_social)):
    #usuario = red_social[i][0]
    #amigos = red_social[i][1]
#for tupla in red_social:
RS_sin_duplicados = []
for usuario, amigos in red_social:
    amigos_sin_duplicados = list(set(amigos))
    RS_sin_duplicados.append((usuario, amigos_sin_duplicados))
print(tuple(RS_sin_duplicados))

#Contar el numero real de amigos de cada usuario
amigos_usu = []
for usurio, amigos in RS_sin_duplicados:
   amigos_usu.append((usuario, len(amigos)))
amigos_usu_tupla = tuple(amigos_usu)
print(amigos_usu_tupla)


#obtener el usuario con más amigos
lista_usuarios = [tupla[0] for tupla in amigos_usu_tupla]
numero_amigos = [tupla[1] for tupla in amigos_usu_tupla]
print(lista_usuarios)
print(numero_amigos)

indice_mas_amigos = numero_amigos.index(max(numero_amigos))
print("El indice de mayor numero de amigos esta en el: ",indice_mas_amigos, "que son", max(numero_amigos))