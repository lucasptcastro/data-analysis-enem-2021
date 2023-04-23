import pandas as pd
import matplotlib.pyplot as plt

class Analises:
    def __init__(self, dataframe, limitador=0) -> None:
        self.df = pd.read_csv(dataframe, sep=";", encoding="ISO-8859-1")

        if limitador != 0: self.df = self.df[0:limitador]
        pass

    def coletar_coluna(self, coluna):
        return self.df[f'{coluna}']
    
    def coletar_valores(self, coluna):
        df = self.df[f'{coluna}']
        return df.value_counts()