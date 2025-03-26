import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset with error handling
def load_data():
    try:
        df = pd.read_csv(r"C:\Hackathon\-E-commerce-Sales-Analysis-Hackathon\sales_data.csv")  
        if 'OrderDate' in df.columns:
            df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.stop()

# Sidebar Filters
st.sidebar.header("Filter Data")
if 'Category' in df.columns:
    selected_category = st.sidebar.multiselect("Select Category", df['Category'].dropna().unique(), key="category_filter")
else:
    selected_category = []

if 'Region' in df.columns:
    selected_region = st.sidebar.multiselect("Select Region", df['Region'].dropna().unique(), key="region_filter")
else:
    selected_region = []

# Apply filters
if selected_category:
    df = df[df['Category'].isin(selected_category)]
if selected_region:
    df = df[df['Region'].isin(selected_region)]

# Main Dashboard
st.title("📊 E-Commerce Sales Dashboard")

# Sales Overview
if 'TotalPrice' in df.columns:
    st.subheader("💰 Sales Overview")
    total_sales = df['TotalPrice'].sum()
    avg_order_value = df['TotalPrice'].mean()
    st.metric("Total Sales", f"${total_sales:,.2f}")
    st.metric("Average Order Value", f"${avg_order_value:,.2f}")

# Top-Selling Products
if 'ProductName' in df.columns:
    st.subheader("🏆 Top 5 Best-Selling Products")
    top_products = df.groupby('ProductName')['TotalPrice'].sum().sort_values(ascending=False).head(5)
    st.bar_chart(top_products)

# Monthly Sales Trend
if 'OrderDate' in df.columns and 'TotalPrice' in df.columns:
    st.subheader("📈 Monthly Sales Trend")
    monthly_sales = df.resample('ME', on='OrderDate')['TotalPrice'].sum()
    monthly_sales.index = monthly_sales.index.strftime('%Y-%m')
    st.line_chart(monthly_sales)

# Customer Segmentation
if 'Gender' in df.columns:
    st.subheader("👥 Customer Spending by Gender")
    gender_spending = df.groupby('Gender')['TotalPrice'].mean()
    fig, ax = plt.subplots()
    sns.barplot(x=gender_spending.index, y=gender_spending.values, ax=ax, palette="coolwarm")
    ax.set_title("Average Spending per Customer by Gender")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Average Total Price")
    st.pyplot(fig)

# Shipping Performance
if 'ShippingStatus' in df.columns:
    st.subheader("🚚 Shipping Performance")
    shipping_status_counts = df['ShippingStatus'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=shipping_status_counts.index, y=shipping_status_counts.values, ax=ax, palette="viridis")
    ax.set_title("Shipping Performance")
    ax.set_xlabel("Shipping Status")
    ax.set_ylabel("Number of Orders")
    st.pyplot(fig)

# Insights
st.write("### 📌 Insights")
st.write("- Focus on best-selling products to boost sales.")
st.write("- Identify top-performing regions for marketing campaigns.")
st.write("- Monitor seasonal trends for better inventory planning.")
st.write("- Improve shipping times to enhance customer satisfaction.")

st.write("---")
st.write("🔍 _Explore the data dynamically using the filters in the sidebar._")
