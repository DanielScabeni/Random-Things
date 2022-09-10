#importando a biblioteca

import pandas as pd
#criar um dataframe

df = pd.DataFrame(
    {
        "coluna1":[90, 45, 78, 34, "Robson"],
        "coluna2":[99, 46, 45, "Cleyton", 78],
        "coluna3":[100, 456, 234, 1345, 1212]
    }
)

print(df)