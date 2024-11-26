from app import app

def test_home_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert "Previsão de Diabetes" in response.data.decode('utf-8')
    assert b"Seu IMC" in response.data

def test_imc_calculation():
    client = app.test_client()
    response = client.post('/imc', data={'altura': '1.70', 'peso': '70'})
    assert response.status_code == 200
    assert b"Resultado:" in response.data

def test_prediction():
    client = app.test_client()

    data = {
        'age': 25,
        'bmi': '24.5',
        'blood_glucose_level': 85,
        'HbA1c_level': '5.5',
        'gender': 'male',
        'hypertension': '0',
        'smoking_history': 'never',
        'heart_disease': '0'
    }

    response = client.post('/predict', json=data)
    print(response.status_code)
    print(response.data)
    assert response.status_code == 200






