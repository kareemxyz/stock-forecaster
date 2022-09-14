# Stock Forecaster - Python

A simple stock closing price forecaster that uses LSTM Neural Networks in Python 3.

## How To Use

This code is meant to be as simple and easy-to-use as possible. Despite this, there are some setup and usage steps (such as installing necessary packages) that are necessary for this code to work. Please read this section carefully.

### 1. Clone the respository

To clone this repoistory using Git, use

```bash
git clone https://github.com/kareemxyz/stock_forecaster.git
```

If you aren't familiar with Git, navigate to the top-left of this page and find the green button labeled "Clone or download". Clicking this and then click "Download ZIP". Extract the contents of the downloaded .zip file.

Open a terminal session and navigate to this folder, using `cd`.

```bash
cd stock_forecaster/
```

### 2. Installing dependencies

We will be installing dependencies using `pip`, the official Python package manager. If you do not have `pip`, I'd recommend checking this [thread](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3/) to install it.

Copy and paste (and run) the following line in your terminal session to install all necessary packages.

```bash
pip3 install numpy && pip3 install pandas-datareader && pip3 install scikit-learn && pip3 install tensorflow
```

### 3. Running

Running this script is straightforward. Simply run in your terminal session:

```bash
python stock_forecaster.py
```

After being prompted to input a stock name, the script will begin to forecast the stock's predicted closing price for the day. Enjoy!
