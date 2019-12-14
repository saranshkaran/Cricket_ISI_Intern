# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:54:34 2019

@author: LENOVO
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:36:59 2019

@author: LENOVO
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:21:23 2019

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
NZ = pd.read_csv(filepath+"\\Eng_2nd_inn.csv", header = 'infer')


balls = NZ.iloc[-10000:-2000,:2]
balls = np.reshape(np.array(balls), (balls.shape[0], 2) )


runs = NZ.iloc[-10000:-1998,-6]
runs = np.reshape(np.array(runs), (runs.shape[0],1) )
index = np.where(np.isnan(runs))
runs = np.delete(runs,index)
runs = np.reshape(np.array(runs), (runs.shape[0],1) )


from sklearn.preprocessing import MinMaxScaler
sc_x = MinMaxScaler()
sc_y = MinMaxScaler()
x_train = sc_x.fit_transform(balls)
y_train = sc_y.fit_transform(runs)
y_train = np.reshape(y_train, (y_train.shape[0],1))
x_train = np.reshape(x_train, (x_train.shape[0], 1, x_train.shape[1]) )




from keras.models import Sequential
model = Sequential()

from keras.layers import Dense, LSTM, Flatten, Dropout

model.add(LSTM(units = 300,return_sequences=True, activation= 'tanh'))
model.add(LSTM(units = 300,return_sequences=True, activation= 'relu'))
#model.add(LSTM(units = 100,return_sequences=True, activation= 'softmax'))


model.add(Dropout(0.5))
model.add(Flatten())



model.add(Dense(units = 1, activation= 'sigmoid'))

model.compile(optimizer = 'rmsprop', loss = 'mse')

model.fit(x_train, y_train, batch_size = 5, epochs = 5)



import json
# lets assume `model` is main model 
model_json = model.to_json()
with open("model_in_json.json", "w") as json_file:
    json.dump(model_json, json_file)

model.save_weights("model_Eng.h5")


balls_test = NZ.iloc[-2000:,:2]
x_test = sc_x.fit_transform(balls_test)
x_test = np.array(x_test)


x_test = np.reshape(x_test, (x_test.shape[0], 2))
x_test = np.reshape(x_test, (x_test.shape[0], 1, x_test.shape[1]) )

actual_runs = NZ.iloc[-2000:,-6]
actual_runs = np.reshape(np.array(actual_runs), (actual_runs.shape[0],1) )
predicted_runs = model.predict(x_test)

#predicted_runs = np.reshape(np.array(predicted_runs), (predicted_runs.shape[0],2) )
#balls = x_y.inverse_transform(predicted_runs)
predicted_runs = sc_y.inverse_transform(predicted_runs)

from matplotlib import pyplot as plt
plt.figure()
balls_test = np.array(balls_test)
balls_test = np.reshape(balls_test[:,0], (balls_test.shape[0], 1))
plt.plot(balls_test,predicted_runs)
plt.plot(balls_test,actual_runs)
plt.title("Eng")
plt.ylabel('runs')
plt.xlabel('balls')
plt.legend(['Predicted Runs','Actual runs'], loc = 'upper left')
plt.savefig("cricket_test_Eng.png")
plt.show()







