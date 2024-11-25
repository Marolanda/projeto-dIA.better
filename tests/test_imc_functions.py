#test_imc_functions.py
import pytest
from utils.imc_functions import validar_peso, validar_altura

# Testes do módulo funções
class TesteFuncoes:

    # Testes unitários para validar_peso
    class TesteValidarPeso:

        # Testes válidos
        def test_deve_aceitar_numero_valido(self):
            assert validar_peso("50") is True
            assert validar_peso("65.5") is True
            assert validar_peso("65,5") is True

        # Testes inválidos
        def test_nao_deve_aceitar_string(self):
            with pytest.raises(ValueError, match="Por favor, insira valores válidos."):
                validar_peso("50kg")

        def test_nao_deve_aceitar_numero_negativo(self):
            assert validar_peso(-10) is False

        def test_deve_lancar_erro_para_espacos_vazios(self):
            with pytest.raises(ValueError, match="Por favor, insira valores válidos."):
                validar_peso("")

        def test_deveria_impedir_valores_com_zero(self):
            assert validar_peso("0") is False

    # Testes unitários para validar_altura
    class TesteValidarAltura:

        # Testes válidos
        def test_deve_aceitar_numero_valido(self):
            assert validar_altura("1.65") is True
            assert validar_altura("1,65") is True

        # Testes inválidos
        def test_nao_deve_aceitar_string(self):
            with pytest.raises(ValueError, match="Por favor, insira valores válidos."):
                validar_altura("50cm")

        def test_nao_deve_aceitar_numero_negativo(self):
            assert validar_altura(-10) is False

        def test_deveria_impedir_valores_com_zero(self):
            assert validar_altura("0") is False

        def test_deveria_lancar_erro_para_espacos_vazios(self):
            with pytest.raises(ValueError, match="Por favor, insira valores válidos."):
                validar_altura("")
