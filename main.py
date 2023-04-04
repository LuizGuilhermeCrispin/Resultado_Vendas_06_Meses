import pandas as pd

# Passo a Passo de solução

# Abrir os 6 arquivos em excel
lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 9995).any():
        vendedor = tabela_vendas.loc [tabela_vendas['Vendas'] > 9995, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc [tabela_vendas['Vendas'] > 9995, 'Vendas'].values[0]
        print(f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas {vendas}')
# Para cada arquivo:

# Verificar se algum valor na coluna Vendas naquele arquivo é maior que R$ 85,00

# Se for maior que R$ 85,00 -> envia um SMS com o nome, mês e as vendas do vendedor

# Caso não seja maior que R$ 85,00, não fazer nada.
