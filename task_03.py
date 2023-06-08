words = ['attribute', 'класс', 'функция', 'type']
i = 0
for word in words:
    i += 1
    try:
        word_bytes = bytes(word, 'ascii')
        print(f'{i}) Type: {type(word_bytes)}, {word_bytes}')
    except UnicodeEncodeError:
        print(f'{i}) Слово "{word}" не может быть переведено в байтовый вид!')
