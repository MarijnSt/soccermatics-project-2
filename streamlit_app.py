import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
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
    category_orders={'role': ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']},
    opacity=style_config['alpha'],
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
    width=750,
    height=600,
)

fig.update_layout(
    legend=dict(
        title=dict(
            text='Roles',
            font=dict(
                size=style_config['sizes']['h3'], 
                color=style_config['colors']['dark']
            ),
            side='top center',
        ),
        x=0.5,
        y=-0.25,
        xanchor='center',
        yanchor='top',
        orientation='h',
        font=dict( 
            color=style_config['colors']['dark']
        ),
    ),
    margin=dict(b=100)
)

st.plotly_chart(fig)