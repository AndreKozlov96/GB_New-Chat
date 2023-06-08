words = ['разработка', 'сокет', 'декоратор']
i = 0
for word in words:
    i += 1
    code_point = word.encode('unicode_escape')
    print(f"\n{i}) code_point: {code_point}\ntype: {type(code_point)}, word: {code_point.decode('unicode_escape')}")
