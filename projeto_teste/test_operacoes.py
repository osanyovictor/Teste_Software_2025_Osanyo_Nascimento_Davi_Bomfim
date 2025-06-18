# test_operacoes.py
import unittest
from operacoes import dividir

class TestOperacoes(unittest.TestCase):

    def test_divisao_por_zero_deve_levantar_excecao(self):
        """Testa o comportamento padrão com assertRaises."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_divisao_valida_com_try_except(self):
        """SOLUÇÃO ACEITA NA ÉPOCA: Ser explícito sobre não esperar uma exceção."""
        try:
            dividir(10, 5)
        except ZeroDivisionError:
            self.fail("A função 'dividir()' levantou ZeroDivisionError inesperadamente!")


    def test_divisao_valida_nao_deve_levantar_excecao(self):
        """
        Testa a divisão com valores válidos.
        O teste passa se nenhuma exceção for levantada
        e o resultado estiver correto.
        """
        resultado = dividir(10, 2)
        self.assertEqual(resultado, 5)

    def test_divisao_por_zero_deve_levantar_excecao2(self):
        """
        Testa se ZeroDivisionError é levantada ao dividir por zero.
        """
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)