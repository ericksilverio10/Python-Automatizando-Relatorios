import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arquivo_excel_1 = 'RELATORIO_PAGAMENTO.xlsx'

df_fevereiro = pd.read_excel(arquivo_excel_1, sheet_name='fevereiro')

estatistica = df_fevereiro.groupby(['Cliente:']).sum()
estatistica_material = df_fevereiro.groupby(['Material:']).sum()

relatorio_cliente = estatistica.loc[:, "Cliente:":"Valor:"]
relatorio_material = estatistica_material.loc[:, "Arte:":"Vídeo:"]

relatorio_cliente.plot(kind='bar')

print(relatorio_cliente)
print(relatorio_material)

plt.show()