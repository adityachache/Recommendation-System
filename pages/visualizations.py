import streamlit as st
import pandas as pd
import plotly.express as px
import gdown

st.set_page_config(
    page_title="Product Analysis Dashboard",
    page_icon="📊",
    layout="wide"  # This makes the app full width
)


# --- Title of the Dashboard ---
st.title("Cluster-Based Product Analysis Dashboard")

st.write("""
This dashboard provides interactive visualizations for analyzing product clusters.
You can explore brand and category distributions, most expensive and cheapest products, 
and overall price distribution.
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
else:
    st.error("Failed to load data from CSV.")

# --- KPIs (Key Performance Indicators) ---
total_products = len(df)
unique_brands = df['brand'].nunique()
total_clusters = df['Cluster'].nunique()

# Display the KPIs in 3 columns
kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric(label="Total Products", value=f"{total_products}")
kpi2.metric(label="Unique Brands", value=f"{unique_brands}")
kpi3.metric(label="Total Clusters", value=f"{total_clusters}")

# --- Row 1: Total Products Sold Per Month Chart ---
products_per_month = df['month'].value_counts().sort_index().reset_index()
products_per_month.columns = ['month', 'total_products']

fig_products_per_month = px.bar(
    products_per_month, 
    x='month', 
    y='total_products', 
    color='total_products', 
    title='Total Products Sold Per Month', 
    text='total_products'
)
fig_products_per_month.update_layout(
    xaxis_title='Month', 
    yaxis_title='Number of Products Sold',
    xaxis=dict(tickmode='linear', tick0=1, dtick=1),
    title_x=0.5  # Center the title
)
st.plotly_chart(fig_products_per_month, use_container_width=True)


# --- Row 1: Two Columns (Charts) ---
col1, col2 = st.columns(2)

# --- Visualization 1: Top 10 Brands Distribution (Bar Chart) ---
with col1:
    # st.subheader("Top 10 Brands Distribution")
    top_10_brands = df['brand'].value_counts().head(10).reset_index()
    top_10_brands.columns = ['brand', 'count']

    fig_brand_dist = px.bar(
        top_10_brands, 
        x='brand', 
        y='count', 
        color='brand', 
        title='Top 10 Brands by Product Count', 
        text='count'
    )
    fig_brand_dist.update_layout(xaxis_title='Brand', yaxis_title='Number of Products')
    st.plotly_chart(fig_brand_dist, use_container_width=True)

# --- Visualization 2: Top 10 Categories Distribution (Bar Chart) ---
with col2:
    # st.subheader("Top 10 Categories Distribution")
    top_10_categories = df['category_code'].value_counts().head(10).reset_index()
    top_10_categories.columns = ['category_code', 'count']

    fig_category_dist = px.bar(
        top_10_categories, 
        x='category_code', 
        y='count', 
        color='category_code', 
        title='Top 10 Product Categories by Product Count', 
        text='count'
    )
    fig_category_dist.update_layout(xaxis_title='Category', yaxis_title='Number of Products')
    st.plotly_chart(fig_category_dist, use_container_width=True)

# --- Row 2: Two Columns (Top 10 Items) ---
col3, col4 = st.columns(2)

# --- Visualization 3: Top 10 Most Expensive Items (Table) ---
with col3:
    st.subheader("Top 10 Most Expensive Items")
    top_10_expensive = df.sort_values(by='price', ascending=False).head(10)
    st.dataframe(top_10_expensive[['item', 'brand', 'category_code', 'price']])

# --- Visualization 4: Top 10 Cheapest Items (Table) ---
with col4:
    st.subheader("Top 10 Cheapest Items")
    top_10_cheapest = df.sort_values(by='price', ascending=True).head(10)
    st.dataframe(top_10_cheapest[['item', 'brand', 'category_code', 'price']])

# --- Row 3: Full Width Histogram of Price Distribution ---
st.subheader("Price Distribution (Histogram)")
fig_price_hist = px.histogram(
    df, 
    x='price', 
    nbins=30, 
    title='Price Distribution of Products'
)
fig_price_hist.update_layout(xaxis_title='Price', yaxis_title='Frequency')
st.plotly_chart(fig_price_hist, use_container_width=True)

