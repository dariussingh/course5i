from django.shortcuts import render
import joblib
import os
import os
import joblib
import pandas as pd
from .models import medicine_exp
import psycopg2

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    model = joblib.load('../prediction_service/model/model.joblib')
    list_ = []
    list_.append(float(request.GET['age']))
    list_.append(float(request.GET['sex']))
    list_.append(float(request.GET['bmi']))
    list_.append(float(request.GET['children']))
    list_.append(float(request.GET['smoker']))
    list_.append(float(request.GET['region']))

    answer = model.predict([list_]).tolist()[0]

    b = medicine_exp(age=request.GET['age'], 
                sex=request.GET['sex'],
                bmi=request.GET['bmi'],
                children=request.GET['children'],
                smoker=request.GET['smoker'],
                region=request.GET['region'],
                charges=answer
                )
    b.save()

    return render(request, 'index.html', {'answer': answer})