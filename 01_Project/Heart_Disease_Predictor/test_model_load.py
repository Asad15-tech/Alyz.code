import pickle

try:
    print("Attempting to load model...")
    with open('best_heart_disease_model.pkl', 'rb') as file:
        model = pickle.load(file)
    print("Model loaded successfully!")
    print(f"Model type: {type(model)}")
except Exception as e:
    print(f"Error loading model: {str(e)}")