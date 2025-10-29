import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Load data
file_path = 'daily_temp.csv'  # Update this with the correct path
data = pd.read_csv(file_path)

# Clean and prepare data
data['태양계 행성'] = pd.to_datetime(data['행성의 위성'].str.strip())
data = data.dropna(subset=['행성의 위성'])
data['태양계 행성'] = data['행성의 위성']

# Calculate yearly statistics
yearly_stats = data.groupby('연도').agg({
    '태양계 행성': 'mean',
    '행성의 위성': 'min',
    '행성과 위성의 거리 차이': 'max'
}).reset_index()

# Streamlit title
st.title("태양계 행성과 그의 위성 사이의 거리")

# User choice for graph type
chart == "distance":
    # Plot line chart
    plt.figure(figsize=(12, 6))
    plt.plot(yearly_stats['연도'], yearly_stats['평균기온(℃)'], label='Average Temperature (℃)', marker='o')
    plt.plot(yearly_stats['연도'], yearly_stats['최저기온(℃)'], label='Minimum Temperature (℃)', marker='o')
    plt.plot(yearly_stats['연도'], yearly_stats['최고기온(℃)'], label='Maximum Temperature (℃)', marker='o')
    plt.xlabel('Year')
    plt.ylabel('Temperature (℃)')
    plt.title('Yearly Temperature Trends')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
