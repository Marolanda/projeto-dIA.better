#test_diabetes_functions.py
import pytest
from utils.diabetes_functions import validar_idade, validarGlicose, valida_input, validaImc

#@pytest.fixture


def test_idade_valida():
    assert validar_idade(19) == "Idade válida."
    assert validar_idade(80) == "Idade válida."

def test_idade_invalida():
    assert validar_idade(150) == "Por favor, insira valores válidos." # Fora do intervalo
    assert validar_idade(-1) == "Por favor, insira valores válidos." # Fora do intervalo
    assert validar_idade(0) == "Por favor, insira valores válidos." # Zero

    assert validar_idade(2.0) == "Idade deve ser um número inteiro." #Número flutuante

def testGlicose_valida():
    assert validarGlicose(70) == "Valor válido."
    assert validarGlicose(110) == "Valor válido."
    
def testGlicose_invalida ():
    assert validarGlicose(130) == "Por favor, insira valores válidos." # Fora do intervalo
    assert validarGlicose(-54.0) == "glicose deve ser um número inteiro." # Fora do intervalo
    assert validarGlicose(0) == "Por favor, insira valores válidos." # Zero

    assert validarGlicose(2.0) == "glicose deve ser um número inteiro." # Número flutuante
        
from utils.diabetes_functions import valida_input, validaImc, validaGenero, validaHipertensao, validaCoracao, validaHistorico

#HEMOGLOBINA
# Teste para valor válido no intervalo (ponto)
def test_valida_input_decimal_valido_ponto():
    assert valida_input("4.5") == "decimal válido"

# Teste para valor válido no intervalo (vírgula)
def test_valida_input_decimal_valido_virgula():
    assert valida_input("6,8") == "decimal válido"

# Teste para valor fora do intervalo (menor que 3)
def test_valida_input_menor_que_3():
    assert valida_input("2.5") == "fora do intervalo"

# Teste para valor fora do intervalo (maior que 9)
def test_valida_input_maior_que_9():
    assert valida_input("10,1") == "fora do intervalo"

# Teste para número negativo (menor que 3)
def test_valida_input_inteiro():
    assert valida_input("-4.0") == "fora do intervalo"

# Teste para número negativo (inválido)
def test_valida_input_inteiro():
    assert valida_input("0") == "inválido"

# Teste para letras (inválido)
def test_valida_input_letras():
    assert valida_input("Dez") == "inválido"

# Teste para número sem decimais (inválido)
def test_valida_input_inteiro():
    assert valida_input("2") == "inválido"

# Teste para valor vazio (inválido)
def test_valida_input_vazio():
    assert valida_input("") == "inválido"


#IMC
def testImc_valida():

    assert validaImc("4.5") == "decimal válido" #Valido com ponto
    assert validaImc("6,8") == "decimal válido" # Válido (vírgula)
    

def testImc_invalido():
    assert validaImc("2.5") == "fora do intervalo" # Fora do intervalo (menor que 3)
    assert validaImc("10,1") == "fora do intervalo" # Fora do intervalo (maior que 9)
    assert validaImc("-4.0") == "inválido" # Número negativo (menor que 3)

    assert validaImc("0") == "inválido" # Número negativo
    assert validaImc("Dez") == "inválido" # Teste para letras 
    assert validaImc("2") == "inválido" # Número sem decimais
    assert validaImc("") == "inválido" # Campo vazio

#genero
def testGenero_valida():

    assert validaGenero("Mulher") is True 
    assert validaGenero("Homem") is True    

def testGenero_invalido():
    with pytest.raises(ValueError, match="Gênero inválido."): 
        validaGenero("Alien")                                 
    with pytest.raises(ValueError, match="Gênero inválido."):
        validaGenero("123")                                   

    assert validaGenero("") == "Campo vazio."                    
    assert validaGenero(None) == "Campo vazio."

#HIPERTENSAO
def testHipertensao_Valida():
    assert validaHipertensao("Sim") is True 
    assert validaHipertensao("Não") is True 

def testHipertensao_invalido():
    with pytest.raises(ValueError, match="inválido."): 
        validaHipertensao("Alta")                                 
    with pytest.raises(ValueError, match="inválido."):
        validaHipertensao("123")                                   

    assert validaHipertensao("") == "Campo vazio."                    
    assert validaHipertensao(None) == "Campo vazio."

#PROBLEMA DE CORAÇÃO
def testCoracao_Valida():
    assert validaCoracao("Sim") is True 
    assert validaCoracao("Não") is True 

def testCoracao_invalido():
    with pytest.raises(ValueError, match="inválido."): 
        validaCoracao("Alta")                                 
    with pytest.raises(ValueError, match="inválido."):
        validaCoracao("123")                                   

    assert validaCoracao("") == "Campo vazio."                    
    assert validaCoracao(None) == "Campo vazio."

#HISTORICO DE FUMO
def testHistorico_Valida():
    assert validaHistorico("Nunca fumei") is True 
    assert validaHistorico("Fumo Atualmente") is True
    assert validaHistorico("Parei de fumar") is True
    assert validaHistorico("Sempre fumei") is True 
    assert validaHistorico("Atualmente não fumo") is True

def testHistorico_invalido():
    with pytest.raises(ValueError, match="inválido."): 
        validaHistorico("Não")                                 
    with pytest.raises(ValueError, match="inválido."):
        validaHistorico("123")                                   

    assert validaHistorico("") == "Campo vazio."                    
    assert validaHistorico(None) == "Campo vazio."