import numpy as np
import pickle

model = pickle.load(open('diabetes prediction sysytem/trained_model.sav' ,'rb'))


input_data =(0	,118,	84,	47,	230,	45.8,	0.551	,31	)
input_np = np.asarray(input_data)
input_data = input_np.reshape(1,-1)


prediction = model.predict(input_data)
if prediction[0]== 1:
    print('person has diabetes')
else:
    print('person is not diabetic')

