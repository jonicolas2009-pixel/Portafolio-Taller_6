Analizador de comentarios

Programa de consola en Python para registrar comentarios de estudiantes sobre sus cursos y analizarlos con operaciones básicas de texto. Desarrollado para el Taller 6 de Lógica de Programación (cadenas, listas y tuplas).

Autor: Joan Nicolas Rey Gomez

Descripción
Los comentarios se guardan en una lista.
Cada comentario se procesa con métodos de cadenas: strip(), lower(), split(), replace(), count() y el operador in.
El resumen de un comentario se almacena en una tupla: (caracteres, palabras, apariciones).
No usa diccionarios, clases, archivos, bases de datos ni librerías externas.
Instrucciones de uso
Instala Python 3.
Descarga o clona este repositorio.
Ejecuta en la terminal:
python main.py
Menú
Opción	Acción
1	Registrar un comentario
2	Mostrar todos los comentarios
3	Buscar comentarios que contengan una palabra
4	Mostrar la cantidad de palabras de cada comentario
5	Contar apariciones de una palabra en un comentario
6	Mostrar el resumen de un comentario (tupla)
7	Salir
Ejemplos de uso

Registrar y buscar

Elija una opcion: 1
Escriba el comentario: Me gusta mucho el curso de Python, el curso es util
Comentario registrado.

Elija una opcion: 3
Palabra a buscar: curso
1 - Me gusta mucho el curso de Python, el curso es util
Busqueda exitosa: 1 comentario(s) encontrado(s).

Elija una opcion: 3
Palabra a buscar: xyz
No se encontraron coincidencias para 'xyz'.

Resumen (tupla)

Tupla: (51, 11, 2)
Caracteres: 51
Palabras: 11
Apariciones de 'curso': 2





Preguntas de análisis:


1. ¿Qué diferencia existe entre aplicar lower() y modificar directamente un carácter
de la cadena?
  -no cambia la cadena original, devuelve una nueva. Hacer frase[0] = "h" da error porque las cadenas son inmutables.

2. ¿Por qué split() devuelve una lista y no una tupla?
  -Porque el resultado suele necesitar cambiarse (agregar, quitar, ordenar palabras), y las listas son modificables.

3. ¿Qué resultado se obtiene con "Hola hola".lower().count("hola")?
  -"Hola hola".lower().count("hola")= da 2 (primero queda "hola hola" y luego cuenta las dos apariciones).

4. ¿Qué ocurriría si se intentara ejecutar resumen[0] = 100?
  -resumen[0] = 100 lanza TypeError, porque las tuplas no admiten asignación a sus elementos

5. ¿En qué situación del ejercicio sería más conveniente una lista que una tupla?
  -cuando los datos cambian, como una lista de compras o los comentarios de este mismo proyecto, donde se agregan elementos todo el tiempo.

