'''
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
'''

# Solucionado por FGF

def fun(p1, p2):
    aux = 0
    anagrama= False
    if (len(p1) == len(p2)) and p1!=p2:
        for x in range(len(p1)):
            if (p1[x] in p2):
                p2 = p2.replace(p1[x],'',1)
                aux += 1
        if aux == len(p1):
            anagrama = True
        else:
            anagrama = False
    return anagrama

palabra1 = 'jamon'
palabra2 = 'anjom'
anagrama = fun(palabra1,palabra2)
print ('Las palabras ' + palabra1 +' y ' +  palabra2 + ' son anagramas: ' + str(anagrama))