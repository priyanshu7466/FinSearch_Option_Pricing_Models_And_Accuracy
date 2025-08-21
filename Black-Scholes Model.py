import numpy as np
import pandas as pd
from scipy.stats import norm
from array import array
from pathlib import Path
ROOT_DIR = Path(__file__).parent

filename3 = ROOT_DIR / 'option-chain-ED-NIFTY-31-Aug-2023.csv'
data3                           = pd.read_csv(filename3)
size3                           =len(data3)

# print(f"Size of Data 3 : {size3}\n\n")

data_STRIKE             =array('i', [0] * size3)
data_IV_CALLS           =array('f', [0] * size3)
data_IV_PUTS            =array('f', [0] * size3)
data_LTP_CALLS          =array('f', [0] * size3)
data_LTP_PUTS           =array('f', [0] * size3)
for i in range(size3):
        value1 = data3.loc[i, "STRIKE"]
        value2 = data3.loc[i, "IV_CALLS"]
        value3 = data3.loc[i, "IV_PUTS"]
        value4 = data3.loc[i, "LTP_CALLS"]
        value5 = data3.loc[i, "LTP_PUTS"]
        data_STRIKE[i]      = int(value1)
        data_IV_CALLS[i]    = float(value2)
        data_IV_PUTS[i]     = float(value3)
        data_LTP_CALLS[i]   = float(value4)
        data_LTP_PUTS[i]    = float(value5)
        # print(f"{i+1} | STRIKE = ", value1, " | IV_CALLS = ", value2, " | IV_PUTS = ", value3)

# Define the Black-Scholes formula for European call option pricing
def black_scholes_call(S, K, r, sigma, T):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def black_scholes_puts(S, K, r, sigma, T):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Define a function to calculate the percentage error between model and real prices
def calculate_percentage_error(model_price, real_price):
    return ((model_price - real_price) / real_price) * 100

S =  19265.80   # Current price of Nifty50 index
r = 0.10        # Risk-free interest rate
T = 0.0164      # Time to expiration

# print("Strike Price\tReal Price (Call)\tSigma (Call)\t\tModel Price (Call)\tPercentage Error (Call)\tReal Price (Call)\tSigma (Call)\t\tModel Price (Call)\tPercentage Error (Call)")
print("Strike Price\tReal Price (Call)\t\tModel Price (Call)\tPercentage Error (Call)\tReal Price (Puts)\t\tModel Price (Puts)\tPercentage Error (Puts)")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")

# Calculate model prices and compare with real prices

for i in range(size3):
    K                = data_STRIKE[i]
    real_price_call  = data_LTP_CALLS[i]
    sigma_call       = data_IV_CALLS[i]/100.0

    real_price_puts  = data_LTP_PUTS[i]
    sigma_puts       = data_IV_PUTS[i]/100.0
    
    model_price_call = black_scholes_call(S, K, r, sigma_call, T)
    percentage_error_call = calculate_percentage_error(model_price_call, real_price_call)

    model_price_puts = black_scholes_puts(S, K, r, sigma_puts, T)
    percentage_error_puts = calculate_percentage_error(model_price_puts, real_price_puts)
    
    # print(f"{K}\t\t{real_price_call:.2f}\t\t{sigma_call:.2f}\t\t{model_price_call:.2f}\t\t{percentage_error_call:.2f}%")
    print(f"{K}\t\t\t{real_price_call:.2f}\t\t\t\t\t{model_price_call:.2f}\t\t\t\t{percentage_error_call:.2f}%\t\t\t\t\t{real_price_puts:.2f}\t\t\t\t\t{model_price_puts:.2f}\t\t\t\t{percentage_error_puts:.2f}%")

