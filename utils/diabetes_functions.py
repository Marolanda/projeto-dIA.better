#diabetes_functions.py
import re
    # Validar idade
def validar_idade(idade):
    if not isinstance(idade, int):
        return "Idade deve ser um número inteiro."
    if idade <= 0:
        return "Por favor, insira valores válidos."
    if idade > 120:
        return "Por favor, insira valores válidos."
    return "Idade válida."
    
    # Validar Glicose
def validarGlicose(glicose):
    if not isinstance(glicose, int):
        return "glicose deve ser um número inteiro."
    if glicose > 0.0 and glicose < 54.0 or glicose > 120.0:
        return "Por favor, insira valores válidos."
    if glicose == 0:
        return "Por favor, insira valores válidos."
    return "Valor válido."

#Validar Hemoglobina
def valida_input(valor):
    valor = valor.strip()
    
    padrao = r"^\d+([.,]\d+)$"
    
    if re.match(padrao, valor):
        valor_float = float(valor.replace(",", "."))
        
        if 3 < valor_float < 9:
            return "decimal válido"
        else:
            return "fora do intervalo"
    else:
        return "inválido"

#Validar IMC
def validaImc(imc):
    imc = imc.strip()
    
    padrao = r"^\d+([.,]\d+)$"
    
    if re.match(padrao, imc):
        imc_float = float(imc.replace(",", "."))
        
        if 10 < imc_float < 100:
            return "decimal válido"
        else:
            return "fora do intervalo"
    else:
        return "inválido"

#GENERO
def validaGenero(genero):
    if not genero:
        return "Campo vazio." 
    
    generoValidados = ["Mulher", "Homem"]
    if genero not in generoValidados:
        raise ValueError("Gênero inválido.")
    return True

#HIPERTENSAO
def validaHipertensao(pressao):
    if not pressao:
        return "Campo vazio." 
    
    pressaoValidada = ["Sim", "Não"]
    if pressao not in pressaoValidada:
        raise ValueError("inválido.")
    return True

#PROBLEMA DE CORAÇÃO
def validaCoracao(problema):
    if not problema:
        return "Campo vazio." 
    
    problemaValidada = ["Sim", "Não"]
    if problema not in problemaValidada:
        raise ValueError("inválido.")
    return True

#HISTORICO DE FUMO
def validaHistorico(fumo):
    if not fumo:
        return "Campo vazio." 
    
    historicoValidado = ["Nunca fumei", "Fumo Atualmente", "Parei de fumar", 
            "Sempre fumei", "Atualmente não fumo"]
    if fumo not in historicoValidado:
        raise ValueError("inválido.")
    return True


