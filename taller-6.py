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
