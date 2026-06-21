# Natural Gas Price Forecasting using Python

## Project Overview

This project analyzes historical natural gas prices and builds a forecasting model capable of estimating gas prices for any date in the past and forecasting prices one year into the future.

The project was completed as part of the JPMorgan Chase Quantitative Research Virtual Experience Program (Forage).

---

## Dataset

The dataset contains monthly natural gas prices from October 2020 to September 2024.

Each observation represents the market price of natural gas delivered at the end of a calendar month.

---

## Objectives

* Analyze historical natural gas price trends
* Identify seasonal patterns in pricing
* Estimate prices for arbitrary dates
* Forecast prices one year beyond the available dataset
* Visualize historical and future prices

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SciPy

---

## Methodology

### Data Preparation

* Loaded historical natural gas price data from CSV
* Converted date values into datetime format
* Transformed dates into numerical values for modeling

### Trend and Seasonality Modeling

Natural gas prices exhibit:

* Long-term upward trend
* Seasonal fluctuations due to heating demand and storage cycles

To capture these patterns, a forecasting model combining:

* Linear Trend Component
* Sinusoidal Seasonal Component

was fitted using SciPy's curve fitting functionality.

### Price Estimation Function

A reusable function was implemented:

```python
estimate_price(date)
```

The function accepts any date and returns an estimated natural gas price.

---

## Results

Key observations:

* Prices generally increase over time.
* Winter months typically show higher prices.
* Summer months typically show lower prices.
* The model successfully captures both trend and seasonality.

---

## Forecast Visualization

![Natural Gas Forecast](forecast.png)

---

## Example Output

```python
estimate_price("2023-06-15")
# Output: 11.11

estimate_price("2025-05-01")
# Output: 12.62
```

---

## Project Structure

```text
NaturalGasProject
│
├── Nat_Gas.csv
├── gas_analysis.py
├── forecast.png
├── README.md
└── requirements.txt
```

---

## Installation

```bash
pip install pandas numpy matplotlib scipy
```

---

## Run Project

```bash
python gas_analysis.py
```

---



## Author

             **Vishal Patidar**


Aspiring Data Analyst passionate about Python, SQL, Power BI, Data Analytics, and Machine Learning.

* GitHub: https://github.com/vishalpatidar0056
* LinkedIn: https://www.linkedin.com/in/vishalpatidar05069664

Feel free to connect with me and explore my projects.


Data Analytics | Python | SQL | Power BI | Machine Learning
