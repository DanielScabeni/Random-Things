print("olá mundo da ciência de dados")

"""este cara aqui e**h para mostrar que podemo**s deixar *textos* longos.

ADICIONANDO O PANDAS NO PROJETO
"""

import pandas as pd

df = pd.DataFrame(
    {
        "coluna1" : [90,45,78,34,991],
        "coluna2" : [99,46,45,78,78],
        "coluna3" : [100,456,234,1345,1212]
    }
)

df

"""Criamos 3 colunas, com arrays contendo 5 registros cada. De vários tipos de dados diferentes.

tirando a média do eixo X (axis = 0)
"""

df.mean(axis=0)

"""tirando a média do eixo Y (axis = 1)"""

df.mean(axis = 1)