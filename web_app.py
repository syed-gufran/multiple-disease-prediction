import numpy as np 
import pickle
import streamlit as st

model = pickle.load(open('/Users/syedgufrahussain/python ml/diabetes prediction sysytem/trained_model.sav', 'rb'))



def diabetes_predictio(input_data):
    
    input_np = np.asarray(input_data)
    input_data = input_np.reshape(1,-1)
    
    prediction = model.predict(input_data)
    if prediction[0]== 1:
        return('person has diabetes')
    else:
        return('person is not diabetic')

def main():
    #title
    st.title('Diabetes Prediction Web App')
     
    #input
    preg = st.text_input('NUmber if pregnancies:')
    gluc = st.number_input("Glucose Level :")
    blood = st.number_input("Blood Pressure Value :")
    skin = st.number_input("Skin Thickness  Value :")
    insulin = st.number_input("Insulin  Value :")
    bmi = st.number_input("BMI Value :")
    pedi = st.number_input("Diabetis Pedigree Function Value :")
    age = st.number_input("age of the person:")

    #code for prediction
    diagnosis = ''

    #creating a button
    if st.button("Diabetes Test Results:"):
        diagnosis = diabetes_predictio([preg, gluc , blood , skin , insulin , bmi , pedi , age])

    st.success(diagnosis)

if __name__=='__main__':
    main()

