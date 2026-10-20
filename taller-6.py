# Lista donde se guardan todos los comentarios (cadenas de texto)
comentarios = []
 
SIGNOS = ".,;:!?¿¡()\"'"
 
 
# ---------------------------------------------------------------
# Funciones de búsqueda
# ---------------------------------------------------------------
def limpiar_texto(texto):
    """Pasa a minusculas y reemplaza los signos de puntuacion por espacios."""
    texto = texto.lower()
    for signo in SIGNOS:
        texto = texto.replace(signo, " ")
    return texto
 
 
def hay_comentarios():
    """Informa si todavia no hay comentarios registrados."""
    if len(comentarios) == 0:
        print("Todavia no hay comentarios registrados.")
        return False
    return True
 
 
def seleccionar_comentario():
    """Muestra los comentarios y pide al usuario que elija uno.
    Devuelve el indice del comentario o -1 si la seleccion no es valida."""
    mostrar_comentarios()
    opcion = input("Numero del comentario: ").strip()
    if not opcion.isdigit():
        print("Debe escribir un numero.")
        return -1
    indice = int(opcion) - 1
    if indice < 0 or indice >= len(comentarios):
        print("Ese comentario no existe.")
        return -1
    return indice
 
 
def crear_resumen(texto, palabra):
    """Procesa un comentario y devuelve una TUPLA con:
    (numero de caracteres, numero de palabras, apariciones de la palabra)."""
    texto = texto.strip()
    cantidad_caracteres = len(texto)
    cantidad_palabras = len(texto.split())
    apariciones = limpiar_texto(texto).split().count(palabra)
    resumen = (cantidad_caracteres, cantidad_palabras, apariciones)
    return resumen

# ---------------------------------------------------------------
# Opciones del menu
# ---------------------------------------------------------------
def registrar_comentario():
    texto = input("Escriba el comentario: ").strip()
    if texto != "":
        comentarios.append(texto)
        print("Comentario registrado.")
    else:
        print("El comentario no puede estar vacio.")
 
 
def mostrar_comentarios():
    if hay_comentarios():
        print("\n--- COMENTARIOS ---")
        for i in range(len(comentarios)):
            print(i + 1, "-", comentarios[i])
 
 
def buscar_comentarios():
    if not hay_comentarios():
        return
    palabra = input("Palabra a buscar: ").strip().lower()
    if palabra == "":
        print("Debe escribir una palabra.")
        return
 
    encontrados = 0
    for i in range(len(comentarios)):
        if palabra in comentarios[i].lower():
            print(i + 1, "-", comentarios[i])
            encontrados += 1
 
    if encontrados == 0:
        print("No se encontraron coincidencias para '" + palabra + "'.")
    else:
        print("Busqueda exitosa:", encontrados, "comentario(s) encontrado(s).")
 
 
def mostrar_cantidad_palabras():
    if not hay_comentarios():
        return
    print("\n--- PALABRAS POR COMENTARIO ---")
    for i in range(len(comentarios)):
        cantidad = len(comentarios[i].split())
        print("Comentario", i + 1, ":", cantidad, "palabras")
 
 
def contar_palabra_en_comentario():
    if not hay_comentarios():
        return
    indice = seleccionar_comentario()
    if indice == -1:
        return
    palabra = input("Palabra a contar: ").strip().lower()
    if palabra == "":
        print("Debe escribir una palabra.")
        return
 
    veces = limpiar_texto(comentarios[indice]).split().count(palabra)
    if veces == 0:
        print("La palabra '" + palabra + "' no aparece en ese comentario.")
    else:
        print("La palabra '" + palabra + "' aparece", veces, "vez/veces.")
     def mostrar_resumen():
    if not hay_comentarios():
        return
    indice = seleccionar_comentario()
    if indice == -1:
        return
    palabra = input("Palabra a buscar en el resumen: ").strip().lower()
    if palabra == "":
        print("Debe escribir una palabra.")
        return
 
    resumen = crear_resumen(comentarios[indice], palabra)
    print("\n--- RESUMEN DEL COMENTARIO", indice + 1, "---")
    print("Tupla:", resumen)
    print("Caracteres:", resumen[0])
    print("Palabras:", resumen[1])
    print("Apariciones de '" + palabra + "':", resumen[2])
 
 
# ---------------------------------------------------------------
# Menu principal
# ---------------------------------------------------------------
def mostrar_menu():
    print("\n===== ANALIZADOR DE COMENTARIOS =====")
    print("1. Registrar un comentario")
    print("2. Mostrar todos los comentarios")
    print("3. Buscar comentarios que contengan una palabra")
    print("4. Mostrar la cantidad de palabras de cada comentario")
    print("5. Contar apariciones de una palabra en un comentario")
    print("6. Mostrar resumen de un comentario")
    print("7. Salir")
 
 
def main():
    opcion = ""
    while opcion != "7":
        mostrar_menu()
        opcion = input("Elija una opcion: ").strip()
 
        if opcion == "1":
            registrar_comentario()
        elif opcion == "2":
            mostrar_comentarios()
        elif opcion == "3":
            buscar_comentarios()
        elif opcion == "4":
            mostrar_cantidad_palabras()
        elif opcion == "5":
            contar_palabra_en_comentario()
        elif opcion == "6":
            mostrar_resumen()
        elif opcion == "7":
            print("Hasta luego.")
        else:
            print("Opcion no valida. Elija un numero del 1 al 7.")
 
 
main()
