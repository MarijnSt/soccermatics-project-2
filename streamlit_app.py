import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from src.styles import style_config
from src.ranking_plot import create_ranking_plot

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
    page_title="Danger Passers",
    page_icon="⚽️",
)

st.title('*Most dangerous passers in the Premier League 2024/2025*')

st.write('')
st.write('This app uses two passing metrics to analyse players:')
st.write('1. **Danger Passes**: passes that end in a shot within 15 seconds.')
st.write('2. **Expected Danger (xD)**: the probability that a pass will be a danger pass and that the following shot will be a goal.')
st.write('The total number of dangers passes and the accumulated xD for each player are then normalized to per 90 stats to be able to compare players with different playing times.')
st.write('')

# Import data
df_summary = pd.read_csv('data/summary.csv')

# Metric map
metric_map = {
    "xD_per_90": "xD per 90",
    "danger_passes_per_90": "Danger passes per 90",
    "xD": "Total xD",
    "danger_passes": "Total number of danger passes",
    "minutes_played": "Number of minutes played",
}

# Sidebar filters
with st.sidebar:
    st.write('**Filter players**')
    role_filter_scatter = st.segmented_control(
        "*Role*", 
        ["All", "Goalkeepers", "Defenders", "Midfielders", "Forwards"],
        default="All"
    )
    minutes_played_filter_scatter = st.number_input("*Minimum minutes played*", min_value=400, max_value=10000, value=400, step=1)

    metric_selection = st.selectbox(
        "*Ranking metric*", 
        metric_map.keys(),
        format_func=lambda x: metric_map[x],
        index=0
    )

# Filter scatter plot data
df_filtered = filter_player_stats(df_summary, role_filter_scatter, minutes_played_filter_scatter)

# Display scatter plot data
st.dataframe(df_filtered)

# Create scatter plot figure
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
        selected=dict(
            marker=dict(
                opacity=1.0,
                size=12
            )
        ),
        unselected=dict(
            marker=dict(
                opacity=style_config['alpha'] - 0.1
            )
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
        text=role_data['short_name'],
        customdata=role_data[['short_name', 'role', 'xD_per_90', 'danger_passes_per_90', 'minutes_played']].values
    ))

# Update scatter plot layout
fig.update_layout(
    title='',
    xaxis_title='Expected Danger (xD) per 90',
    yaxis_title='Danger Passes per 90',
    width=750,
    height=600,
    showlegend=False
)

# Display scatter plot with selection enabled
selected_points = st.plotly_chart(fig, on_select="rerun", selection_mode="points")

# Show detailed information for selected player in scatter plot
if selected_points and 'selection' in selected_points:    
    for point in selected_points['selection']['points']:
        player_data = point['customdata']
        player_name = player_data[0]
        player_role = player_data[1]
        xd_per_90 = player_data[2]
        danger_passes_per_90 = player_data[3]
        minutes_played = player_data[4]
        
        # Find the full player data
        player_row = df_filtered[df_filtered['short_name'] == player_name].iloc[0]

        st.header(f"*{player_name}*")
        
        # Display player information in columns
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Role", f"{player_role}")
            st.metric("Minutes Played", f"{minutes_played:,}")
        
        with col2:
            st.metric("xD per 90", f"{xd_per_90:.2f}")
            st.metric("Danger Passes per 90", f"{danger_passes_per_90:.2f}")
        
        with col3:
            if 'xD' in player_row:
                st.metric("Total xD", f"{player_row['xD']:.2f}")
            if 'danger_passes' in player_row:
                st.metric("Total Danger Passes", f"{player_row['danger_passes']}")
        
        with col4:
            st.metric("Total xD", f"{player_row['xD']:.2f}") # goals
            st.metric("Total Danger Passes", f"{player_row['danger_passes']}") # assists


st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.header('*Top 10 players*')

st.write('')
st.write('Everyone likes to look at the rankings, so here you go!')
st.write('Below is a list of the top 10 players in the league based on the filters and ranking metric you selected in the sidebar.')
st.write('')

# Get metric column name

# Create top 10
df_sorted = df_filtered.sort_values(by=metric_selection, ascending=True).tail(10).reset_index(drop=True)

# Create ranking plot
fig = create_ranking_plot(df_sorted, role_filter_scatter, minutes_played_filter_scatter, metric_selection, metric_map[metric_selection])

# Display ranking plot
st.pyplot(fig)