from django.shortcuts import render
import pickle
import os
import numpy as np
from django.conf import settings

from sklearn.ensemble import RandomForestClassifier

def load_model():
    try:
        from sklearn.ensemble import RandomForestClassifier
        
        # Create a model with some default rules
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        
        def custom_predict(X):
            predictions = []
            for row in X:
                # Extract features
                age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal = row
                
                # Define risk factors based on medical knowledge
                risk_score = 0
                
                # Age factor (age > 50 increases risk)
                if age > 50:
                    risk_score += 1
                if age > 60:
                    risk_score += 1
                
                # Blood pressure factor (normal range: 90-120)
                if trestbps > 140:  # High BP
                    risk_score += 2
                
                # Cholesterol factor (normal range: < 200)
                if chol > 240:  # High cholesterol
                    risk_score += 2
                
                # Chest pain type factor
                if cp > 0:  # Any chest pain other than typical angina
                    risk_score += 2
                
                # Exercise induced angina
                if exang == 1:
                    risk_score += 2
                
                # ST depression
                if oldpeak > 2:
                    risk_score += 2
                
                # Number of major vessels
                risk_score += int(ca)
                
                # Thalassemia
                if thal >= 2:
                    risk_score += 1
                
                # Fasting blood sugar
                if fbs == 1:  # > 120 mg/dl
                    risk_score += 1
                
                # Make prediction based on risk score
                predictions.append(1 if risk_score >= 6 else 0)
            
            return np.array(predictions)
        
        # Replace the predict method with our custom implementation
        model.predict = custom_predict
        return model, None
            
    except Exception as e:
        error_msg = f"Error creating model: {str(e)}"
        print(error_msg)
        return None, error_msg
            
    except Exception as e:
        error_msg = f"Error loading model: {str(e)}"
        print(error_msg)
        return None, error_msg

def home(request):
    return render(request, 'home.html')

def predict(request):
    prediction_result = None
    error_message = None
    
    if request.method == 'POST':
        try:
            # Get form data
            age = float(request.POST.get('age'))
            sex = float(request.POST.get('sex'))
            cp = float(request.POST.get('cp'))
            trestbps = float(request.POST.get('trestbps'))
            chol = float(request.POST.get('chol'))
            fbs = float(request.POST.get('fbs'))
            restecg = float(request.POST.get('restecg'))
            thalach = float(request.POST.get('thalach'))
            exang = float(request.POST.get('exang'))
            oldpeak = float(request.POST.get('oldpeak'))
            slope = float(request.POST.get('slope'))
            ca = float(request.POST.get('ca'))
            thal = float(request.POST.get('thal'))
            
            # Load model
            model, error = load_model()
            if model is None:
                error_message = f"Error: {error}"
            else:
                try:
                    # Make prediction
                    features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, 
                                        thalach, exang, oldpeak, slope, ca, thal]])
                    prediction = model.predict(features)
                    prediction_result = "High Risk" if prediction[0] == 1 else "Low Risk"
                except Exception as e:
                    error_message = f"Error during prediction: {str(e)}"
        except Exception as e:
            error_message = f"Error making prediction: {str(e)}"
            
    return render(request, 'predict.html', {
        'prediction': prediction_result,
        'error_message': error_message
    })
        
    return render(request, 'predict.html', {'prediction': prediction_result})

from .models import BlogPost, AboutPage

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def about(request):
    about_content = AboutPage.objects.first()
    return render(request, 'about.html', {'about': about_content})
