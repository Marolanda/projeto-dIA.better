from app import app, preprocess_input, model_columns, formatar_numeros

def test_preprocess_input():
    client = app.test_client()
    
    data = {
        'age': 25,
        'bmi': 24.5,
        'blood_glucose_level': 85,
        'HbA1c_level': 5.5,
        'gender': 'male',
        'hypertension': 0,
        'smoking_history': 'never',
        'heart_disease': 0
    }

    response = client.post('/predict', json=data)  
    print(response.status_code)
    print(response.data)
    assert response.status_code == 200

def test_formatar_numeros():
    form_data = {'bmi': '25,5', 'HbA1c_level': '5,5'}
    formatted_data = formatar_numeros(form_data)
    assert formatted_data['bmi'] == 25.5
    assert formatted_data['HbA1c_level'] == 5.5
