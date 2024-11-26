#imc_functions.py
import re

def validar_peso(peso):
    # Verifica se o peso é uma string e tenta converter para número
    if isinstance(peso, str):
        peso = peso.replace(',', '.')  # Substitui a vírgula por ponto

    # Verifica se o peso é um número ou se a string corresponde ao padrão de número com vírgula ou ponto decimal
    regex = r'^[0-9]+([,.][0-9]+)?$'
    if not isinstance(peso, (int, float)) and not re.match(regex, str(peso)):
        raise ValueError("Por favor, insira valores válidos.")

    # Converte a string para número, caso necessário
    peso = float(peso)

    # Verifica se o peso é negativo
    if peso <= 0:
        return False

    return True


def validar_altura(altura):
    # Verifica se a altura é uma string e tenta converter para número
    if isinstance(altura, str):
        altura = altura.replace(',', '.')  # Substitui a vírgula por ponto

    # Verifica se a altura é um número ou se a string corresponde ao padrão de número com vírgula ou ponto decimal
    regex = r'^[0-9]+([,.][0-9]+)?$'
    if not isinstance(altura, (int, float)) and not re.match(regex, str(altura)):
        raise ValueError("Por favor, insira valores válidos.")

    # Converte a string para número, caso necessário
    altura = float(altura)

    # Verifica se a altura é negativa
    if altura <= 0:
        return False

    return True
