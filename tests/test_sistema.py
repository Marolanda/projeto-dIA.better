from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Inicializar o WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Acessar o site
    driver.get("https://dia-better.onrender.com/")

    # Esperar até que o título da página seja carregado
    WebDriverWait(driver, 10).until(EC.title_contains("dIA.better"))

    #PAGINA IMC
    submit_button = driver.find_element(By.ID, "botao_azul")
    submit_button.click()

    # Esperar pela página IMC
    WebDriverWait(driver, 10).until(EC.title_contains("Calcule seu IMC"))

    # Preencher os campos de IMC
    peso_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input_peso")))
    peso_element.send_keys("70")  # Exemplo de peso

    altura_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input_altura")))
    altura_element.send_keys("1.75")  # Exemplo de altura

    # Submeter o formulário para calcular IMC
    calcular_imc_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "botao_azul")))
    calcular_imc_button.click()

    # Esperar pelo resultado do cálculo do IMC
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "resultado_imc")))

    # Agora, volte para a página inicial
    driver.get("https://dia-better.onrender.com/")  # Volta à página inicial

    # Confirmar se voltou à página inicial
    WebDriverWait(driver, 10).until(EC.title_contains("dIA.better"))

    # Esperar pelo resultado e imprimir
    resultado_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "resultadoL")))
    print(f"Resultado da predição: {resultado_element.text}")

    # Preencher os campos de entrada (inputs)
    idade_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input_idade")))
    idade_element.send_keys("30")

    #imc_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input_imc")))
    #imc_element.clear()  # Limpa qualquer valor previamente preenchido
    #imc_element.send_keys("25.4")  # Define um valor correto para o IMC

    glicose_element = driver.find_element(By.ID, "input_glicose")
    glicose_element.send_keys("100")

    hba1c_element = driver.find_element(By.ID, "input_hba1c")
    hba1c_element.send_keys("5.7")

    # Selecionar opções nos menus dropdown
    genero_select = driver.find_element(By.NAME, "gender")
    Select(genero_select).select_by_visible_text("Homem")

    hipertensao_select = driver.find_element(By.NAME, "hypertension")
    Select(hipertensao_select).select_by_visible_text("Sim")

    fumo_select = driver.find_element(By.NAME, "smoking_history")
    Select(fumo_select).select_by_visible_text("Nunca fumei")

    coracao_select = driver.find_element(By.NAME, "heart_disease")
    Select(coracao_select).select_by_visible_text("Não")

    # Enviar o formulário usando o texto do botão
    submit_button = driver.find_element(By.XPATH, "//button[text()='Calcular']")
    submit_button.click()

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    driver.quit() #Fechar o navagador após executar tudo