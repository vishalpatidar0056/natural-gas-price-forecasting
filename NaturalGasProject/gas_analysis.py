import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load dataset

df = pd.read_csv("Nat_Gas.csv")

# Convert dates

df['Dates'] = pd.to_datetime(
df['Dates'],
format='%m/%d/%y'
)

# Create numerical representation of dates

df['Days'] = (
df['Dates'] - df['Dates'].min()
).dt.days

x = df['Days'].values
y = df['Prices'].values

# Trend + Seasonality Model

def seasonal_model(x, a, b, c, d):
    return (
        a
        + b*x
        + c*np.sin(
            2*np.pi*x/365 + d
        )
    )   
params, _ = curve_fit(
seasonal_model,
x,
y
)

# Price estimation function

def estimate_price(date_string):
    # parse input date string to Timestamp
    date = pd.to_datetime(date_string)

    days = (
        date - df['Dates'].min()
    ).days

    predicted_price = seasonal_model(
        days,
        *params
    )

    return round(
        float(predicted_price),
        2
    )

# Example predictions

print("Historical Estimate:")
print(
estimate_price("2023-06-15")
)

print("Future Estimate:")
print(
estimate_price("2025-05-01")
)

# Forecast one additional year

future_dates = pd.date_range(
start=df['Dates'].max(),
periods=13,
freq='ME'
)

future_days = (
future_dates - df['Dates'].min()
).days

future_prices = seasonal_model(
future_days,
*params
)

# Visualization

plt.figure(figsize=(12,6))

plt.plot(
df['Dates'],
df['Prices'],
marker='o',
label='Historical Prices'
)

plt.plot(
future_dates,
future_prices,
'--',
label='Forecast Prices'
)

plt.title(
'Natural Gas Price Forecast'
)

plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.legend()

plt.savefig("forecast.png")
plt.show()
