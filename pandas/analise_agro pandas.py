import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Caminho do CSV
arquivo = r"C:\Users\Aluno\Desktop\teste\dados_agro.csv"

df = pd.read_csv(arquivo)

print("Colunas do CSV:", list(df.columns))
print("\nPrévia dos dados:")
print(df.head()) python analise_agro.py

col_temp = 'temperatura (°C)'
col_hum = 'umidade (%)'
col_lux  = 'luminosidade (lux)'
col_bomba = 'bomba_ligada'
col_timestamp = 'data_hora'

df[col_temp] = pd.to_numeric(df[col_temp], errors='coerce')
df[col_lux] = pd.to_numeric(df[col_lux], errors='coerce')
df[col_hum] = pd.to_numeric(df[col_hum], errors='coerce')

mask_bomba_on = df[col_bomba].astype(str).str.strip().str.lower() == 'sim'
if mask_bomba_on.sum() == 0:
    print("\nAviso: não foram encontradas linhas com bomba ligada (valor 'Sim').")
else:
    media_umidade = df.loc[mask_bomba_on, col_hum].mean()
    print(f"\nMédia de umidade quando bomba ligada: {media_umidade:.2f}%")

if col_lux in df.columns and col_temp in df.columns:
    corr = df[col_lux].corr(df[col_temp])
    print(f"\nCorrelação (Pearson) entre {col_lux} e {col_temp}: {corr:.3f}")

    plt.figure(figsize=(8,5))
    sns.scatterplot(x=col_lux, y=col_temp, data=df)
    plt.xlabel(col_lux)
    plt.ylabel(col_temp)
    plt.title("Dispersão: Luminosidade vs Temperatura")
    plt.tight_layout()
    plt.show()
else:
    print("\nColuna de luminosidade ou temperatura não encontrada — verifique os nomes.")

if col_timestamp in df.columns:
    df[col_timestamp] = pd.to_datetime(df[col_timestamp], errors='coerce')
    df['hour'] = df[col_timestamp].dt.hour

    def periodo_da_hora(h):
        if pd.isna(h):
            return None
        h = int(h)
        if 0 <= h <= 5:
            return 'Madrugada (00-05)'
        if 6 <= h <= 11:
            return 'Manhã (06-11)'
        if 12 <= h <= 17:
            return 'Tarde (12-17)'
        return 'Noite (18-23)'

    df['periodo'] = df['hour'].apply(periodo_da_hora)

    grouped = df.groupby('periodo')[col_temp].agg(['count','mean','min','max','std']).dropna()
    grouped['range'] = grouped['max'] - grouped['min']
    print("\nVariação de temperatura por período:")
    print(grouped)

    if not grouped.empty:
        periodo_max = grouped['range'].idxmax()
        print(f"\nPeríodo com maior variação (max-min): {periodo_max}")

    order = ['Madrugada (00-05)','Manhã (06-11)','Tarde (12-17)','Noite (18-23)']
    plt.figure(figsize=(8,5))
    sns.boxplot(x='periodo', y=col_temp, data=df, order=order)
    plt.title("Distribuição de Temperatura por Período")
    plt.xlabel("Período")
    plt.ylabel(col_temp)
    plt.tight_layout()
    plt.show()
else:
    print("\nColuna de data/hora não encontrada — não é possível calcular períodos do dia.")
