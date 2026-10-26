'''Una biblioteca tiene una lista de libros y sus autores. Crea un programa que tome la lista
de libros y sus autores como una lista de tuplas, donde cada tupla contiene el título del
libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del
libro y el apellido del autor.
Pista: Tus datos de entrada podrían ser así —>'''

lista_libros = [("El aleph", "Jorge Luis Borges"), 
                ("Cien años de soledad", "Gabriel Garcia Márquez"),
                ("La ciudad y los perros", "Mario Vargas Llosa")]

titulosYapellidos = []
for tupla in lista_libros:
    titulo, autor = tupla
    apellido = autor.split()[-1]
    titulosYapellidos.append((titulo, apellido))
print(titulosYapellidos)
    

                                    
        
