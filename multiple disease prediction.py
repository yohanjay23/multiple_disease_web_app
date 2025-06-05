# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 17:16:50 2025

@author: YShanuka
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open(r"C:/Users/HP/Desktop/Multiple Disease Prediction System/Diabetes_model.sav", "rb"))

heart_disease_model = pickle.load(open(r"C:/Users/HP/Desktop/Multiple Disease Prediction System/Heart_disease_model.sav", "rb"))

parkinson_disease_model = pickle.load(open(r"C:/Users/HP/Desktop/Multiple Disease Prediction System/Parkinson_model.sav", "rb"))


#sidebar for navigation

with st.sidebar:
    
    selected = option_menu("Multiple Disease Prediction System",
                           ["Diabetes Prediction",
                            "Heart Disease Prediction",
                            "Parkinson Prediction"],
                           
                           icons = ['activity', 'heart', 'person'],
                           
                           default_index = 0)
    
    
if (selected == "Diabetes Prediction"):
    
    # page title
    st.title("Diabetes Prediction Using ML")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    
    with col2:
        BloodPressure = st.text_input("Blood Pressure Value")
        
    with col3:
        Glucose = st.text_input("Glucose Level")    
       
    with col1:
        SkinThickness = st.text_input("Skin Thikness")
    
    with col2:
        Insulin = st.text_input("Insulin Level")

    with col3:
        BMI = st.text_input("BMI Value")

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Value")
    
    with col2:
        Age = st.text_input("Age")
        
    
    #for prediction
    diab_diagnosis = ''
    
    # A button for prediction
    
    if st.button ('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

        if diab_prediction[0] == 1:
            
            diab_diagnosis = 'The person is Diabetic'
        else:
            
            diab_diagnosis = 'The person is not Diabetic'
            
    st.success(diab_diagnosis)                
            
            
if (selected == "Heart Disease Prediction"):
    
    st.title("Heart Disease Prediction Using ML")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age")
        
    with col2:
        sex = st.text_input("Sex")
    
    with col3:
        cp = st.text_input("Chest Pain Type")
        
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
        
    with col2:
        chos = st.text_input("Serum Cholestoral in mg/dl")

    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl") 
        
    with col1:
        restecg = st.text_input("Resting Electrocardiographic Results (values 0,1,2)")
    
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")    
        
    with col3:
        exang = st.text_input("Exercise Induced Angina")
        
    with col1:
        oldpeak = st.text_input("Oldpeak ") 
        
    with col2:
        slope = st.text_input("Slope of the Peak ")
 
    with col3:
        ca = st.text_input("Number of Major Vessels")
        
    with col1:
        thal = st.text_input("Thal")
        
    
    heart_diagnosis = ''

    if st.button ('Heart Test Result'):
        head_prediction = heart_disease_model.predict([age, sex, cp, trestbps, chos, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])

        if head_prediction[0] == 1:
            
            heart_diagnosis = 'The person has not a heart disease'
            
        else:
            
            heart_diagnosis = 'The person has a heart disease'
            
    st.success(heart_diagnosis)     
    

if (selected == "Parkinson Prediction"):
    
    st.title("Parkinson Prediction Using ML")    
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1 :
        name = st.text_input("Name")
        
    with col2 :
        MDVP_Fo_Hz	= st.text_input("MDVP:Fo(Hz)")  
        
    with col3 :
        MDVP_Fhi_Hz = st.text_input("MDVP:Fhi(Hz)") 

    with col1 :
        MDVP_Flo_Hz = st.text_input("MDVP:Flo(Hz)") 

    with col2 :
        MDVP_Jitter = st.text_input("MDVP:Jitter(%)") 

    with col3 :
        MDVP_Jitter_Abs = st.text_input("MDVP:Jitter(Abs)") 
    
    with col1 :
        MDVP_RAP = st.text_input("MDVP:RAP") 

    with col2 :
        MDVP_PPQ = st.text_input("MDVP:PPQ") 
        
    with col3 :
        Jitter_DDP = st.text_input("Jitter:DDP") 
            
    with col1 :
        MDVP_Shimmer = st.text_input("MDVP:Shimmer")         

    with col2 :
        MDVP_Shimmer_dB = st.text_input("MDVP:Shimmer(dB)") 
    
    with col3 :
        Shimmer_APQ3 = st.text_input("Shimmer:APQ3") 
        
    with col1 :
        Shimmer_APQ5 = st.text_input("Shimmer:APQ5")     
    
    with col2 :
        MDVP_APQ = st.text_input("MDVP:APQ") 
        
    with col3 :
        Shimmer_DDA	 = st.text_input("Shimmer:DDA")     

    with col1 :
        NHR	 = st.text_input("NHR") 

    with col2 :
        HNR	 = st.text_input("HNR")     

    with col3 :
        RPDE	 = st.text_input("RPDE") 

    with col1 :
        DFA	 = st.text_input("DFA") 

    with col2 :
        spread1	 = st.text_input("Spread 1")
        
    with col3 :
        spread2	 = st.text_input("Spread 2")
        
    with col1 :
        D2	 = st.text_input("D2")
        
    with col2 :
        PPE	 = st.text_input("PPE")
            
        
    parkinson_diagnosis = ''

    if st.button ('Parkinson Test Result'):
        parkinson_prediction = parkinson_disease_model.predict([name, MDVP_Fo(Hz), MDVP_Fhi(Hz), MDVP_Flo(Hz), MDVP_Jitter, MDVP_Jitter(Abs), MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer(dB), Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE])

        if head_prediction[0] == 1:
            
            heart_diagnosis = 'The person has not a heart disease'
            
        else:
            
            heart_diagnosis = 'The person has a heart disease'
            
    st.success(parkinson_diagnosis)







