def encoding_01():
    arquivo_palavras = open("palavras.txt", enconding="latin_1")
    conteudo = arquivo_palavras.readlines()
    print(conteudo)
if __name__ == "__main__":
    encoding_01()

