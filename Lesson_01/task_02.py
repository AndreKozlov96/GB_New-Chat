words = ['class', 'function', 'method']
i = 0
for word in words:
    i += 1
    word_bytes = bytes(word, 'ascii')
    print(f'{i}) type: {type(word_bytes)}, {word_bytes}, len: {len(word_bytes)}')
