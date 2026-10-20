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

