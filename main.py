from Analyzer.text_analyzer import (
    count_words,
    count_characters,
    count_paragraphs,
    count_sentences,
    longest_paragraphs,
    longest_sentences,
    longest_word,
    
)

text = '''
El reloj de la cocina marcaba las 3:17 cuando una pequeña luz azul apareció detrás del refrigerador. Nadie en la casa la vio al principio, excepto el gato, que dejó de lamerse la pata y se quedó mirando fijamente. La luz parpadeó tres veces, como si estuviera intentando recordar algo, y luego desapareció dejando en el aire un olor extraño, parecido a lluvia sobre metal caliente.\n\nEl gato bajó lentamente de la silla y se acercó al rincón con una cautela inexplicable. Olfateó el piso, movió la cola una sola vez y soltó un maullido tan bajo que parecía venir de otra habitación. Entonces, desde dentro de la pared, alguien respondió con tres golpes suaves.
'''
print ('Palabras : ', count_words(text))
print ('Caracteres : ', count_characters(text))
print ('Parrafos : ', count_paragraphs(text))
print ('Oraciones : ', count_sentences(text))
print ('Palabra mas larga : ', longest_word(text))
print ('Oracion mas Larga : ', longest_sentences(text))
print ('Parrafo mas largo : ', longest_paragraphs(text))