# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:35:15 2019

@author: LENOVO
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 04:02:33 2019

@author: LENOVO
"""


import pandas as pd
import os
import numpy as np 
filepath = os.getcwd()
NZ = pd.DataFrame()
NZ = pd.read_csv(filepath+"\\NZ_1st_inn.csv", header = 'infer')


balls = NZ.iloc[-30000:-2000,:2]
balls_test = np.reshape(np.array(balls), (balls.shape[0], 2) )

runs = NZ.iloc[-30000:-2000,-6]
runs = np.reshape(np.array(runs), (runs.shape[0],1) )




from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
x_train = sc.fit_transform(balls)
y_train = sc.fit_transform(runs)
y_train = np.reshape(y_train, (y_train.shape[0],1))
x_train = np.reshape(x_train, (x_train.shape[0], 1, x_train.shape[1]) )




from keras.models import Sequential
model = Sequential()

from keras.layers import Dense, LSTM, Flatten, Dropout

model.add(LSTM(units = 10,return_sequences=True, activation= 'tanh'))


model.add(Dropout(0.5))
model.add(Flatten())



model.add(Dense(units = 1, activation= 'sigmoid'))

model.compile(optimizer = 'rmsprop', loss = 'mse')

model.fit(x_train, y_train, batch_size = 1, epochs = 5)



import json
# lets assume `model` is main model 
model_json = model.to_json()
with open("model_in_json.json", "w") as json_file:
    json.dump(model_json, json_file)

model.save_weights("model.h5")
