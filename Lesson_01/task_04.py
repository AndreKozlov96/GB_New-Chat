words = ['разработка', 'администрирование', 'protocol', 'standard']
i = 0
for word in words:
    i += 1
    word_bytes = word.encode('utf-8')
    word_decode = word_bytes.decode('utf-8')
    print(f'{i}) Encode: type: {type(word_bytes)}, {word_bytes}\nDecode: type: {type(word_decode)}, {word_decode}\n')
