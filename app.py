from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

data = pd.read_csv('data_final.csv') 

app = Flask(__name__)

# Carregar o modelo treinado e as colunas usadas durante o treinamento
with open('diabetes_model.pkl', 'rb') as file:
    model, model_columns = pickle.load(file)

# Função para converter a entrada do formulário em formato adequado para o modelo
def preprocess_input(data):
    # Criar um DataFrame com as colunas esperadas
    df = pd.DataFrame(data, index=[0])
    
    # Converte as colunas categóricas em variáveis dummy
    df = pd.get_dummies(df, drop_first=True)

    # Adiciona colunas ausentes com valor 0
    for col in model_columns:
        if col not in df.columns:
            df[col] = 0
    
    # Garantir que todas as colunas esperadas estejam presentes
    df = df[model_columns]

    
    return df

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/outra')
def outra_pagina():
    return render_template('imc.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Coletar dados do formulário
        data = {
            'gender': request.form['gender'],
            'age': int(request.form['age']),
            'hypertension': request.form['hypertension'],
            'heart_disease': request.form['heart_disease'],
            'smoking_history': request.form['smoking_history'],
            'bmi': float(request.form['bmi']),
            'HbA1c_level': float(request.form['HbA1c_level']),
            'blood_glucose_level': int(request.form['blood_glucose_level'])
        }
        
        # Convertendo para o formato adequado
        processed_data = preprocess_input(data)
        
        # Realizar a previsão
        prediction = model.predict(processed_data)[0]
        
        if float(prediction) == 0.0:
            resultado_texto = "É improvável haver diabetes."
        elif float(prediction) == 1.0:
            resultado_texto = "É provável que haja diabetes."
        else:
        # Caso ocorra um valor decimal inesperado
            resultado_texto = f"Resultado: {round(float(prediction), 2)}"

        # Retornar o resultado
        return render_template('index.html', prediction=resultado_texto)
    except Exception as e:
        # Log de erro
        return f'Ocorreu um erro: {e}'

if __name__ == '__main__':
    app.run(debug=True)