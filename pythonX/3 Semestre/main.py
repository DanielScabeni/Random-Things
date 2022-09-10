import csv
# abrir o arquivo

with open("filmes.csv") as arquivo:
   #print(type(arquivo))
    tabela = csv.reader(arquivo, delimiter = ",")

    next(tabela)

    for linha in tabela:
       titulo = linha[0]
       ano = linha[1]
       n_oscar= linha[2]

       print(f"o filme {titulo}, lançado no {ano} VENCEU {n_oscar} oscars")

