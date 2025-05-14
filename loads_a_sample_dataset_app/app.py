import streamlit as st
import pandas as pd
import numpy as np

# Set page title with emoji
st.title("📊 Data Analytics Dashboard 🚀")

# Add a welcome message with emojis
st.markdown("Welcome to the Data Analytics App! Explore the dataset below 😊✨")

# Create a sample dataset
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
    'Price': [999, 699, 299, 199, 49],
    'Sales': [150, 300, 200, 100, 500]
}
df = pd.DataFrame(data)

# Display dataset with emoji
st.subheader("📋 Dataset")
st.dataframe(df)

# Add a slider to filter data by price
st.subheader("🔍 Filter by Price")
price_filter = st.slider("Select maximum price:", 0, 1000, 500)
filtered_df = df[df['Price'] <= price_filter]
st.write(f"Showing products with price ≤ ${price_filter} 💸")
st.dataframe(filtered_df)

# Add a line chart
st.subheader("📈 Sales Trend")
st.line_chart(filtered_df[['Sales']])

# Add a footer with emojis
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Data Analytics App  by Hira Khalid")