import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

print("Building dummy LSTM Model...")
model = Sequential()
model.add(LSTM(units=50, activation='relu', return_sequences=True, input_shape=(100, 1)))
model.add(Dropout(0.2))

# Reduced complexity: fewer layers
model.add(LSTM(units=50, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')

# 5. Save Model
model_filename = "stock_sentiment_model.keras"
model.save(model_filename)
print(f"Model saved as {model_filename}")
