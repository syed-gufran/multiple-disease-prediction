
import pickle
import streamlit as st
import streamlit_option_menu as option_menu
import numpy as np

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
parkinson_model = pickle.load(open('parkinsons_model.sav', 'rb'))
heart_model = pickle.load(open('heart_disease_model.sav', 'rb'))

 
with st.sidebar:
    selected = option_menu.option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Machine Learning')
    
    col1 , col2 , col3 = st.columns(3)
    with col1:
        preg = st.number_input('Number of Pregnancies:', value=0)
    with col2:
        gluc = st.number_input("Glucose Level:", value=100)
    with col3:
        blood = st.number_input("Blood Pressure Value:", value=70)
    with col1:
        skin = st.number_input("Skin Thickness Value:", value=20)
    with col2:      
        insulin = st.number_input("Insulin Value:", value=80)
    with col3:
        bmi = st.number_input("BMI Value:", value=25.0)
    with col1:
        pedi = st.number_input("Diabetes Pedigree Function Value:", value=0.5)
    with col2:
        age = st.number_input("Age of the Person:", value=30)
    
    diab_prediction = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[preg, gluc, blood, skin, insulin, bmi, pedi, age]])
        if diab_prediction[0] == 1:
            st.success('The person is Diabetic')
        else:
            st.success('The person is Not Diabetic')

if selected == 'Parkinson Prediction':
    st.title('Parkinson Disease Prediction using Machine Learning')

    col1, col2, col3 = st.columns(3)
    with col1:
        fo = st.number_input('MDVP:Fo(Hz):', value=140.0)
    with col2: 
        fhi = st.number_input('MDVP:Fhi(Hz):', value=160.0)
    with col3:
        flo = st.number_input('MDVP:Flo(Hz):', value=80.0)
    with col1: 
        jitt = st.number_input('MDVP:Jitter(%):', value=0.003)
    with col2:
        jita = st.number_input('MDVP:Jitter(Abs):', value=0.00002)
    with col3:
        rap = st.number_input('MDVP:RAP:', value=0.002)
    with col1:
        ppq = st.number_input('MDVP:PPQ:', value=0.002)
    with col2:
        ddp = st.number_input('Jitter:DDP:', value=0.006)
    with col3:
        shd = st.number_input('MDVP:Shimmer:', value=0.01)       
    with col1:
        shdb = st.number_input('MDVP:Shimmer(dB):', value=0.1)
    with col2:
        apq3 = st.number_input('Shimmer:APQ3:', value=0.005)
    with col3:
        apq5 = st.number_input('Shimmer:APQ5:', value=0.007)           
    with col1:
        apq = st.number_input('MDVP:APQ:', value=0.01)
    with col2:
        dda = st.number_input('Shimmer:DDA:', value=0.02)
    with col3:
        nhr = st.number_input('NHR:', value=0.01)
    with col1:
        hnr = st.number_input('HNR:', value=22.0)
    with col2:    
        rpde = st.number_input('RPDE:', value=0.4)
    with col3:
        dfa = st.number_input('DFA:', value=0.7)      
    with col1:
        spread1 = st.number_input('Spread1:', value=-4.0)
    with col2:
        spread2 = st.number_input('Spread2:', value=0.2)
    with col3:
        d2 = st.number_input('D2:', value=2.0)
    with col1:
        ppe = st.number_input('PPE:', value=0.1)    

    parkinson_prediction = ''

    if st.button('Parkinson Test Result'):  
        parkinson_prediction = parkinson_model.predict([[fo, fhi, flo, jitt, jita, rap, ppq, ddp, shd, shdb, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])
        if parkinson_prediction[0] == 1:
            st.success('The person is at risk of Parkinson Disease')
        else:
            st.success('The person is not at risk of Parkinson Disease')


if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using Machine Learning')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age:', value=30)
    with col2: 
        sex = st.number_input('Sex:', value=1)
    with col3:
        cp = st.number_input('Chest Pain Type:', value=0)
    with col1:
        trestbps = st.number_input('Resting Blood Pressure:', value=120)
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl:', value=200)
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl:', value=0)
    with col1:
        restecg = st.number_input('Resting Electrocardiographic Results:', value=0)
    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved:', value=150)
    with col3:
        exang = st.number_input('Exercise Induced Angina:', value=0)
    with col1:
        oldpeak = st.number_input('ST Depression Induced by Exercise:', value=1.0)
    with col2:
        slope = st.number_input('Slope of the Peak Exercise ST Segment:', value=2)
    with col3:
        ca = st.number_input('Number of Major Vessels (0-3):', value=0)
    with col1:
        thal = st.number_input('Thalassemia:', value=1)
 
    heart_prediction = ''
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_prediction[0] == 1:
            st.success('The person is at risk of Heart Disease')
        else:
            st.success('The person is not at risk of Heart Disease')
