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

df_summary['point_size'] = 30

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
    size='point_size',
    size_max=7.5,
    hover_name='short_name',
    hover_data={
        'xD_per_90': False,
        'danger_passes_per_90': False,
        'role': False,
        'point_size': False
    },
    labels={
        'xD_per_90': 'Expected Danger (xD) per 90',
        'danger_passes_per_90': 'Danger Passes per 90',
    },
    width=750,
    height=600,
)

# Remove legend
fig.update_layout(
    legend=dict(
        visible=False,
        # title=dict(
        #     text='',
        #     font=dict(
        #         size=style_config['sizes']['h3'], 
        #         color=style_config['colors']['dark']
        #     ),
        # ),
        # y=0.5,
        # yanchor='middle',
        # font=dict( 
        #     size=style_config['sizes']['h3'],
        #     color=style_config['colors']['dark']
        # ),
    ),
)

st.plotly_chart(fig)