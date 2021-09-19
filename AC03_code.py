class Calculadora:
    def __init__(self, n1, n2, operador):
        self.n1 = n1
        self.n2 = n2
        self.operador = operador

    def soma(self):
        return self.n1 + self.n2

    def subtração(self):
        return self.n1 - self.n2

    def multiplicação(self):
        return self.n1 * self.n2

    def divisão(self):
        return self.n1 / self.n2


class Operacao(Calculadora):
    def __init__(self, n1, n2, operador):
        self.n1 = n1
        self.n2 = n2
        self.operador = operador

    def executar(self):
        if self.operador == "+":
            return(Operacao.soma(self))
        elif self.operador == "-":
            return(Calculadora.subtração())
        elif self.operador == "*":
            return(Calculadora.multiplicação())
        elif self.operador == "/":
            return(Calculadora.divisão())


teste = Operacao(10, 5, "+")

teste.executar()
