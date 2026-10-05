# Microsoft Stock Price Forecasting & Trends

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-blueviolet.svg)](https://seaborn.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

This repository analyzes historical stock prices of Microsoft using time series techniques, moving averages, and trend visualization[cite: 18].

---

## Project Workflow
1. **Data Loading & Preprocessing**: Reading historical stock records (`Microsoft_Stock.csv`), converting date strings to datetime objects, and sorting chronologically[cite: 18].
2. **Feature Engineering**: Computing 50-day (`MA_50`) and 200-day (`MA_200`) moving averages to analyze market trends[cite: 18].
3. **Exploratory Data Analysis & Visualization**: Plotting closing prices and moving averages using Seaborn and Matplotlib[cite: 18].
4. **Web Application**: Interactive deployment interface built with Streamlit.

---

## Getting Started & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/microsoft-stock-trends.git](https://github.com/YOUR_USERNAME/microsoft-stock-trends.git)
   cd microsoft-stock-trends
