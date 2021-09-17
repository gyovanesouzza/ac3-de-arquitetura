import abc
from unittest import TestCase, main


class Calculadora(object):
    def calcular(self, valor1, valor2, operador):
        operacao = OperacaoFabrica().criar(operador)
        if(not operacao):
            return 0
        else:
            return operacao.executar(valor1, valor2)


class OperacaoFabrica(object):
    def criar(self, operador):
        if(operador == 'soma'):
            return Soma()
        elif(operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()


class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass


class Soma(Operacao):
    def executar(self, valor1, valor2):
        return valor1 + valor2


class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 - valor2


class Divisao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 / valor2


class Testes(TestCase):
    calculador = Calculadora()

    def test_soma(self):
        self.assertNotEqual(Calculadora().calcular(254, 0, 'soma'), 255)

    def test_soma2(self):
        self.assertEqual(Calculadora().calcular(-5, 15, 'soma'), 10)

    def test_soma3(self):
        self.assertEqual(Calculadora().calcular(25, 6, 'soma'), 31)

    def test_divisao(self):
        self.assertNotEqual(Calculadora().calcular(125, 5, 'divisao'), 20)
    def test_divisao2(self):
        self.assertNotEqual(Calculadora().calcular(5, 3, 'divisao'), 0.34)
    def test_divisao3(self):
        self.assertEqual(Calculadora().calcular(3, 1.5, 'divisao'), 2)

    def test_subtracao(self):
        self.assertNotEqual(Calculadora().calcular(-15, -20, 'subtracao'), -35)
    def test_subtracao2(self):
        self.assertEqual(Calculadora().calcular(192, 30, 'subtracao'), 162)
    def test_subtracao3(self):
        self.assertNotEqual(Calculadora().calcular(6, 5, 'subtracao'), 0)

    def test_soperacao_errada(self):
        self.assertEqual(Calculadora().calcular(-15, -20, 'Soma'), 0)

    def test_soperacao_errada2(self):
        self.assertEqual(Calculadora().calcular(6, 5, 'subtrcao'), 0)
        
    def test_soperacao_errada3(self):
       self.assertEqual(Calculadora().calcular(192, 30, 'divisa'), 0)


if __name__ == '__main__':
    main()
