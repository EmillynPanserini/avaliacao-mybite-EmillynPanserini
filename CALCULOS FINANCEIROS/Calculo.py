import math

class Calculo:
    def __init__(self, capital_inicial, taxa_juros, tempo):
        if capital_inicial < 0 or taxa_juros < 0 or tempo < 0:
            raise ValueError("Valores devem ser maiores que 0")

        self.valor_juros = None
        self.montante_final = None
        self.valor_presente = None
        self.valor_futuro = None
        self.capital_inicial = float(capital_inicial)
        self.tempo = float(tempo)
        self.taxa_juros = float(taxa_juros)



    def calcular_valor_juros_simples(self):
        self.valor_juros = self.capital_inicial * self.taxa_juros *  self.tempo
        return self.valor_juros

    def calcular_montante_final_simples(self):
        self.montante_final = self.capital_inicial + self.valor_juros
        return  self.montante_final

    def calcular_valor_juros_composto(self):
        self.valor_juros = self.montante_final - self.capital_inicial
        return self.valor_juros

    def calcular_montante_final_juros_composto(self):
        self.montante_final = self.capital_inicial * math.pow(1+self.taxa_juros, self.tempo)
        return self.montante_final

    def calcular_valor_presente(self, valor_futuro_calcular):
        if self.tempo == 0:
            self.valor_presente = valor_futuro_calcular
        else:
            self.valor_presente =  valor_futuro_calcular / ((1 + self.taxa_juros) ** self.tempo)
        return self.valor_presente

if __name__=="__main__":

    investimento = Calculo(1000, 0.02, 3)

    juros_gerados_simples = investimento.calcular_valor_juros_simples()
    montante_final_simples = investimento.calcular_montante_final_simples()
    print(f"Valor juros simples: {juros_gerados_simples}")
    print(f"Valor montante final do juros simples: {montante_final_simples}")

    juros_gerados_composto = investimento.calcular_valor_juros_composto()
    montante_final_composto = investimento.calcular_montante_final_juros_composto()
    print(f"Valor juros composto: {juros_gerados_composto}")
    print(f"Valor juros simples: {montante_final_composto}")

    valor_presente_gerado = investimento.calcular_valor_presente(1000)
    print(f"Valor presente: {valor_presente_gerado}")