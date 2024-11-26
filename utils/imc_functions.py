#imc_functions.py
import re

def validar_peso(peso):
    if isinstance(peso, str):
        peso = peso.replace(',', '.')  

    regex = r'^[0-9]+([,.][0-9]+)?$'
    if not isinstance(peso, (int, float)) and not re.match(regex, str(peso)):
        raise ValueError("Por favor, insira valores válidos.")

    peso = float(peso)

    if peso <= 0:
        return False

    return True


def validar_altura(altura):
    if isinstance(altura, str):
        altura = altura.replace(',', '.') 

    regex = r'^[0-9]+([,.][0-9]+)?$'
    if not isinstance(altura, (int, float)) and not re.match(regex, str(altura)):
        raise ValueError("Por favor, insira valores válidos.")

    altura = float(altura)

    if altura <= 0:
        return False

    return True
