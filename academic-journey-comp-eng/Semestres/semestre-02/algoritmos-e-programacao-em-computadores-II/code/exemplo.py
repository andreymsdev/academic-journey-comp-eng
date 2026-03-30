def readFile(filename):
    with open(filename, 'r', encoding='utf-8') as infile:
        content = infile.read()
    wordList = content.split()
    print(wordList)
    return len(wordList), len(content)

n_words, n_chars = readFile('../r.txt')
print(f"Número de palavras: {n_words}, Número de caracteres: {n_chars}")
