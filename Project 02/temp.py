# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

#loading the saved model
loaded_model=pickle.load(open('C:/Users/ASUS/Project 02/trained_model.sav','rb'))
input_data =np.asarray([5,166,72,19,175,25.8,0.587,51]).reshape(1,-1)
prediction =loaded_model .predict(input_data)
print(prediction)
if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')
