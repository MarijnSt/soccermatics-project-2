import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from src.styles import style_config

# Functions
@st.cache_data
def filter_player_stats(df_player_stats, role_filter, minutes_played_filter):
    df = df_player_stats.copy()

    # Role filter
    if role_filter != "All":
        if role_filter == "Goalkeepers":
            df = df[df["role"] == "Goalkeeper"]
        elif role_filter == "Defenders":
            df = df[df["role"] == "Defender"]
        elif role_filter == "Midfielders":
            df = df[df["role"] == "Midfielder"]
        elif role_filter == "Forwards":
            df = df[df["role"] == "Forward"]

    # Minutes played filter
    if minutes_played_filter:
        df = df[df["minutes_played"] >= minutes_played_filter]

    return df

# PAGE CONFIG
st.set_page_config(
    page_title="Danger passers",
    page_icon="⚽️",
)

st.title('Most dangerous passers in the Premier League 2024/2025')

# Import data
df_summary = pd.read_csv('data/summary.csv')

# Sidebar filters
with st.sidebar:
    st.subheader("Filter players")
    role_filter = st.segmented_control(
        "Role", 
        ["All", "Goalkeepers", "Defenders", "Midfielders", "Forwards"],
        default="All"
    )
    minutes_played_filter = st.number_input("Minimum minutes played", min_value=400, max_value=10000, value=400, step=1)

# Filter data
df_filtered = filter_player_stats(df_summary, role_filter, minutes_played_filter)

# Display data
st.dataframe(df_filtered)


# Create the figure
fig = go.Figure()

# Add traces for each role
for role in df_filtered['role'].unique():
    role_data = df_filtered[df_filtered['role'] == role]
    
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
                     '<span style="color:white"><b>%{x:.2f}</b> xD per 90</span><br>' +
                     '<span style="color:white"><b>%{y:.2f}</b> danger passes per 90</span><br>' +
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