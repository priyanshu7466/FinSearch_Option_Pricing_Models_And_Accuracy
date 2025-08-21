# Here is a Python script that assesses
# the accuracy of the Black-Scholes
# Model by comparing its calculated
# option prices to the real option
# prices derived from Nifty50 index
# options.

import numpy as np
from scipy.stats import norm

# For Calculating the price for Call Option
def black_scholes_call(S, K, r, sigma, T):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def black_scholes_puts(S, K, r, sigma, T):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Terms Used
# Stores the choice of user
i = int(input("1 for Call, 2 for Put : "))

# Current Nifty50-Index : 25 Aug (Closing)
S = float(input("S (19265.80)\t: ")) # 19265.80

# Strike Price
K = float(input("K\t: "))

# Risk-Free Intrest Rate (Current -> 10%)
r = float(input("r\t: ")) # 0.10

# Implied Volatility (in Percents)
sigma = float(input("sigma\t: "))

# Time for Expiration (in Years from 25 Aug to 31 Aug, Total 6 days)
T = float(input("T (0.0164)\t: ")) # 0.0164

if (i==1):
    print(black_scholes_call(S, K, r, sigma, T))
else :
    print(black_scholes_puts(S, K, r, sigma, T))
# Should be close to LTP_Call