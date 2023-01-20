import os
path = input ("Dame la ruta:")
dirCount = 0
phrase = ""

for ruta, dirs, files in os.walk(path):
    for directories in dirs:
        if int(directories)%5 == 0:
            dirCount += 1
            phrase += directories + " "
    for ficheros in files:
        nombreFichero = os.path.basename(ficheros)
        phrase += nombreFichero + " "

print('Número de directorios divisibles por cinco: ', dirCount)

# Crear la frase sin ordenar
phrase = phrase.strip()
print("Frase sin ordenar:", phrase)

# Crear el diccionario
word_lengths = {len(word): word for word in phrase.split()}
print("Diccionario:", word_lengths)

# Ordenar la frase
phrase_list = phrase.split()
phrase_list.sort()
phrase_ordered = " ".join(phrase_list)
print("Frase ordenada:")
print(phrase_ordered)
