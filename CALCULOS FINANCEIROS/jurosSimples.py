class JurosSimples:
    def __init__(self):
        self.valorJuros = 0
        self.montanteFinal = 0

    def calcularJurosImples(self, capitalInicial,  taxaJuros, valorJuros, montanteFinal, tempo):
        self.valorJuros = capitalInicial * taxaJuros *  tempo
        montanteFinal = capitalInicial + valorJuros
