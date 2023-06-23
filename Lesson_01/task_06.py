from chardet import detect

words = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as f:
    for word in words:
        f.write(word + '\n')
with open('test_file.txt', 'r') as f:
    for line in f:
        word_utf_bytes = bytes(line, 'utf-8')
        print(word_utf_bytes.decode('utf-8'), end='')
        print(f"coding: {detect(word_utf_bytes)['encoding']}\n")
