import pickle

# load the saved encoder and model
def load_artifacts(encoder_path='models/encoder.pkl', model_path = 'models/gradient_model.pkl'):
    with open(encoder_path, 'rb') as f:
        encoder = pickle.load(f)
    
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    return encoder, model


# encodes the input data and returns the churn prediction and probability
def predict_churn(input_data, encoder, model):
    for col, enco in encoder.items():
       input_data[col] = enco.transform(input_data[col])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return prediction, probability