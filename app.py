import streamlit as st
import pandas as pd
import gdown

# Main Page Title
st.title("Welcome to the Product Cluster Analysis App")

# Introduction
st.write("""
This app allows you to explore product clusters, visualize data, 
and gain insights into product categories, pricing, and trends. 

Use the sidebar to navigate to:
- **Recommendations**: Get product recommendations.
- **Visualizations**: Explore product clusters and visual data.
""")

# --- Download CSV from Google Drive ---
@st.cache_data
def load_data_from_drive():
    file_id = '1RsybmkRpYDNcVx6G3bb_qW-fgFD-4NBq'  # Replace with your actual file ID
    url = f'https://drive.google.com/uc?id={file_id}&export=download'
    output = 'clusters.csv'
    gdown.download(url, output, quiet=False)
    
    try:
        df = pd.read_csv(output)
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        df = pd.DataFrame()  # Empty DataFrame to prevent crashing
    return df

# --- Load Data ---
df = load_data_from_drive()

# --- Display Data ---
if not df.empty:
    st.success("Cluster Data Loaded")
    st.dataframe(df)
else:
    st.error("Failed to load data from CSV.")