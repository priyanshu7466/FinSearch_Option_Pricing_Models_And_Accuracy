<div align=center>
  
# FinSearch's Black-Scholes Model Demonstration
<img src='https://badges.strrl.dev/visits//Aviteshmurmu19/FinSearch-Final'></img> <img src='https://img.shields.io/badge/Python-badge?logo=PYTHON&logoColor=yellow&labelColor=grey&color=blue'></img> <img src='https://img.shields.io/github/repo-size/Aviteshmurmu19/FinSearch-Final'></img>

## A Python script that assesses the accuracy of the Black-Scholes Model by comparing its calculated option prices to the real option prices derived from Nifty50 index options.
</div>

### Black-Scholes Model Demo.py
#### Arguments:
i -- Stores the choice of user

S -- Current Nifty50-Index : 25 Aug (Closing)

sigma -- Implied Volatility (in Percents)

K -- Strike Price

r -- Risk-Free Intrest Rate (Current -> 10%)

T -- Time for Expiration (in Years from 25 Aug to 31 Aug, Total 6 days)

#### Returns:
Calculated price of option using BSM

### Black-Scholes Model.py
#### Returns
Percentage Error between calculated price and actual price of options.
