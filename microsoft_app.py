import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Microsoft Stock Analysis App", layout="centered")

st.title("Microsoft Stock Price Forecasting & Trends")
st.write(
    "Bu uygulama, Microsoft hisse senedi geçmiş fiyat verilerini zaman serisi teknikleri, hareketli ortalamalar ve trend görselleriyle analiz eder."
)

@st.cache_data
def load_data():
    df = pd.read_csv("Microsoft_Stock.csv", low_memory=False)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").reset_index(drop=True)
    df["MA_50"] = df["Close"].rolling(window=50).mean()
    df["MA_200"] = df["Close"].rolling(window=200).mean()
    return df

try:
    df = load_data()
    
    st.subheader("Hisse Senedi Veri Seti Önizlemesi")
    st.dataframe(df.head())

    st.subheader("Hisse Senedi Trend Grafikleri")
    chart_type = st.selectbox(
        "Grafik Türü Seçin",
        ["Kapanış Fiyatı Zaman Serisi", "Hareketli Ortalamalarla (MA_50 ve MA_200) Analiz"]
    )
    
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 5))
    
    if chart_type == "Kapanış Fiyatı Zaman Serisi":
        ax.plot(df["Date"], df["Close"], label="Closing Price", color="royalblue")
        ax.set_title("Microsoft Stock Closing Prices Over Time", fontsize=14, fontweight="bold")
        ax.set_ylabel("Price (USD)", fontsize=12)
    else:
        ax.plot(df["Date"], df["Close"], label="Close Price", color="lightgray", alpha=0.7)
        ax.plot(df["Date"], df["MA_50"], label="50-Day Moving Average", color="orange")
        ax.plot(df["Date"], df["MA_200"], label="200-Day Moving Average", color="crimson")
        ax.set_title("Microsoft Stock Price with Moving Averages", fontsize=14, fontweight="bold")
        ax.set_ylabel("Price (USD)", fontsize=12)
        
    ax.set_xlabel("Date", fontsize=12)
    ax.legend()
    st.pyplot(fig)

except Exception as e:
    st.error(f"Veri yüklenirken veya işlenirken bir hata oluştu: {e}")