class Juros_simples:
    def __init__(self):
        self.valor_juros = 0
        self.montante_final = 0

    def calcular_juros_simples(self, capital_inicial,  taxa_juros, valor_juros, montante_final, tempo):
        self.valor_juros = capital_inicial * taxa_juros *  tempo

        return self.valor_juros
    def calcular_montante_final(self, capital_inicial, valor_juros):
        self.montante_final = capital_inicial + valor_juros
        return  self.montante_final