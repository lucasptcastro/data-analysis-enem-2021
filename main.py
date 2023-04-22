import pandas as pd

microdados_enem = pd.read_csv('./MICRODADOS_ENEM_2021.csv', sep=";", encoding="ISO-8859-1")
print(microdados_enem.head())