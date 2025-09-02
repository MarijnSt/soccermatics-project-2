import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from src.styles import style_config

# PAGE CONFIG
st.set_page_config(
    page_title="Danger passers",
    page_icon="⚽️",
)

st.title('Most dangerous passers in the Premier League 2024/2025')

# Import data
df_summary = pd.read_csv('data/summary.csv')

# Display data
#st.dataframe(df_summary)

# Create the figure
fig = go.Figure()

# Add traces for each role
for role in df_summary['role'].unique():
    role_data = df_summary[df_summary['role'] == role]
    
    fig.add_trace(go.Scatter(
        x=role_data['xD_per_90'],
        y=role_data['danger_passes_per_90'],
        mode='markers',
        marker=dict(
            color=style_config['colors'][role.lower()],
            size=10,
            opacity=style_config['alpha']
        ),
        name=role,
        hovertemplate='<b style="color:white">%{text}</b><br>' +
                     '<span style="color:white">' + role + '</span><br>' +
                     '<extra></extra>',
        hoverlabel=dict(
            bgcolor=style_config['colors'][role.lower()],
            font_color='white',
            font_size=12
        ),
        text=role_data['short_name']
    ))

# Update layout
fig.update_layout(
    title='',
    xaxis_title='Expected Danger (xD) per 90',
    yaxis_title='Danger Passes per 90',
    width=750,
    height=600,
    showlegend=False
)

st.plotly_chart(fig)