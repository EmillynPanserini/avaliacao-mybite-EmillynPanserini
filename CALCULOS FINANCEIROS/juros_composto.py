import math

class Juros_composto:
    def __init__(self):
        self.montante_final = 0
        self. valor_juros = 0

    def calcular_valor_jurosl(self, capital_inicial):
        self.valor_juros = self.montante_final - capital_inicial
        return self.valor_juros

    def calcular_montante_final(self, capital_inicial, taxa_juros,tempo):
        self.montante_final = capital_inicial * math.pow(1+taxa_juros, tempo)