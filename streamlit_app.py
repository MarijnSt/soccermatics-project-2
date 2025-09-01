import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from src.styles import style_config

print(style_config['colors'])

# PAGE CONFIG
st.set_page_config(
    page_title="Danger passers",
    page_icon="⚽️",
)

st.title('Most Dangerous Passers in the Premier League 2024/2025')

# Import data
df_summary = pd.read_csv('data/summary.csv')

# Display data
#st.dataframe(df_summary)

# Create scatter plot
fig = px.scatter(
    df_summary,
    x='xD_per_90',
    y='danger_passes_per_90',
    color='role',
    color_discrete_map={
        'Forward': style_config['colors']['forward'],
        'Midfielder': style_config['colors']['midfielder'],
        'Defender': style_config['colors']['defender'],
        'Goalkeeper': style_config['colors']['goalkeeper']
    },
    hover_name='short_name',
    hover_data={
        'xD_per_90': False,
        'danger_passes_per_90': False,
        'role': False
    },
    labels={
        'xD_per_90': 'Expected Danger (xD) per 90',
        'danger_passes_per_90': 'Danger Passes per 90',
    },
)

st.plotly_chart(fig)