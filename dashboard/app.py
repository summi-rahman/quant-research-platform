import streamlit as st
import requests
import pandas as pd

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Quant Research Dashboard", layout="wide")

st.title("📊 Quant Research Dashboard")

# -------------------------------
# DESCRIPTION
# -------------------------------
st.markdown("""
### 📌 What this dashboard shows

This dashboard compares **two trading strategies vs the market**:

- 🔵 **Volatility Strategy**  
  Trades when market volatility is high and trend is positive  

- 🟢 **Mean Reversion Strategy**  
  Buys when price drops below its average (expects rebound)  

- ⚫ **Market Benchmark**  
  Baseline performance of the asset  

---

👉 **Goal:** Compare performance, risk, and consistency across strategies
""")

# -------------------------------
# BUTTON
# -------------------------------
if st.button("🚀 Run Strategy"):

    try:
        res = requests.get("http://127.0.0.1:8000/run-strategy")

        # -------------------------------
        # ERROR HANDLING
        # -------------------------------
        if res.status_code != 200:
            st.error(f"API Error: {res.status_code}")
            st.text(res.text)
        else:
            data = res.json()

            if "error" in data:
                st.error(data["error"])
            else:
                # -------------------------------
                # METRICS SECTION
                # -------------------------------
                st.subheader("📈 Strategy Performance Metrics")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("### 🔵 Volatility Strategy")
                    st.write(data["volatility_strategy"]["metrics"])

                with col2:
                    st.markdown("### 🟢 Mean Reversion Strategy")
                    st.write(data["mean_reversion_strategy"]["metrics"])

                # -------------------------------
                # DATAFRAME FOR CHART
                # -------------------------------
                df = pd.DataFrame({
                    "Volatility Strategy": data["volatility_strategy"]["equity_curve"],
                    "Mean Reversion Strategy": data["mean_reversion_strategy"]["equity_curve"],
                    "Market": data["market"]
                })

                # Normalize market for comparison
                df["Market"] = df["Market"] / df["Market"].iloc[0]

                # -------------------------------
                # CHART SECTION
                # -------------------------------
                st.subheader("📊 Equity Curve Comparison")

                st.markdown("""
                **How to read this chart:**
                - **X-axis** → Time (trading days)  
                - **Y-axis** → Growth of $1 investment  
                - Higher line = better performance  
                """)

                st.line_chart(df)

    except Exception as e:
        st.error(f"Error: {e}")