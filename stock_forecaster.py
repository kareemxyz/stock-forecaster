# Predicts a stock's closing price
# Kareem Elewa, 9 September 2022

import os
import numpy as np
import pandas_datareader as web
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler

# **************PLEASE READ THE README.md FOR USE INSTRUCTIONS**************

def get_filtered_closing_data(stock, days_before=0):
    try:
        raw_dataframe = web.DataReader(stock, data_source="yahoo")
        closing_data = raw_dataframe.filter(["Close"])
        data_set = closing_data[-days_before:].values
        return scaler.fit_transform(data_set), stock
    except:
        print("Failed to fetch stock data! Please input a valid stock.")
        return get_filtered_closing_data(input("Stock: ").upper())


def get_training_data(filtered_data):
    x = []
    y = []
    for i in range(60, len(filtered_data)):
        x.append(filtered_data[i - 60:i, 0])
        y.append(filtered_data[i, 0])
    x, y = np.array(x), np.array(y)
    x = np.reshape(x, (x.shape[0], x.shape[1], 1))
    return (x, y)


def train_model(x, y):
    x_shape = (x.shape[1], 1)

    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=x_shape))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))
    model.compile(optimizer="adam", loss="mean_squared_error")
    os.system(os.name == 'nt' and 'cls' or 'clear')
    model.fit(x, y, batch_size=1, epochs=1)
    return model


def get_predictated_closing_price(stock):
    filtered_data, stock = get_filtered_closing_data(stock)
    training_data = get_training_data(filtered_data)
    model = train_model(*training_data)

    last_60_days = np.array(last_60_days)
    reshape = (last_60_days, (last_60_days.shape[0], last_60_days.shape[1], 1))

    last_price = scaler.inverse_transform([last_60_days[0, -1]])[0, 0]
    predicted_price = model.predict(np.reshape(*reshape))
    predicted_price = scaler.inverse_transform(predicted_price)[0, 0]
    difference = predicted_price - last_price

    os.system(os.name == 'nt' and 'cls' or 'clear')
    print(f"Stock Closing Prediction For {stock}")
    print("Last Price:")
    print('{:.2f}'.format(last_price), "USD")
    print("\nPredicted Closing Price:")
    print('{:.2f}'.format(predicted_price), "USD")
    print(f"{'{:+.2f}'.format(difference)} ({'{:+.2f}'.format((difference / last_price) * 100)}%)\n")


if __name__ == "__main__":
    scaler = MinMaxScaler(feature_range=(0, 1))
    os.system(os.name == 'nt' and 'cls' or 'clear')
    print("Please read README.md for use instructions.")
    selected_stock = input("Stock: ").upper()
    get_predictated_closing_price(selected_stock)