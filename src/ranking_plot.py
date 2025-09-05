import matplotlib.pyplot as plt
from src.styles import style_config
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
from pathlib import Path


def create_ranking_plot(df, position_filter, minutes_played_filter, metric):
    """
    Create a ranking plot for a given metric and filters.

    Parameters
    ----------
    df: pd.DataFrame
        The dataframe with the players to plot.
    position_filter: list
        List of positions to include in the plot.
    minutes_played_filter: int
        The minimum minutes played to include in the plot.
    metric: str
        The metric to plot.

    Returns
    -------
    fig: plt.Figure
        The figure object.
    """

    # Init plt styling
    plt.rcParams.update({
        'font.family': style_config['fonts']['light'].get_name(),
        'font.size': style_config['sizes']['p'],
        'text.color': style_config['colors']['dark'],
        'axes.labelcolor': style_config['colors']['dark'],
        'axes.edgecolor': style_config['colors']['dark'],
        'xtick.color': style_config['colors']['dark'],
        'ytick.color': style_config['colors']['dark'],
        'grid.color': style_config['colors']['dark'],
        'figure.facecolor': style_config['colors']['background'],
        'axes.facecolor': style_config['colors']['background'],
    })

    # Create figure
    fig = plt.figure(figsize=(12, 1 + 0.6 * len(df)))      # Increase height of figure based on number of rows in ranking
    gs = fig.add_gridspec(3, 1, height_ratios=[0.1, 0.8, 0.1])       # 2 rows, 1 column, with height ratios for title, plot, legend

    # Init axis
    heading_ax = fig.add_subplot(gs[0])
    main_ax = fig.add_subplot(gs[1])
    legend_ax = fig.add_subplot(gs[2])

    # Hide axis
    heading_ax.axis('off')
    legend_ax.axis('off')

    # Hide spines
    main_ax.spines['top'].set_visible(False)
    main_ax.spines['bottom'].set_visible(False)
    main_ax.spines['left'].set_visible(False)
    main_ax.spines['right'].set_visible(False)

    # Remove axis ticks
    main_ax.set_yticklabels([])
    main_ax.set_yticks([])
    main_ax.set_xticks([])

    # Title
    heading_ax.text(
        0, 
        0.5, 
        f"Top 10 players in the Premier League 2024/2025",
        fontsize=style_config['sizes']['h1'],
        fontproperties=style_config['fonts']['medium_italic'],
        ha='left', 
        va='bottom'
    )

    # Subtitle
    heading_ax.text(
        0, 
        0, 
        f'{metric} by players with at least {minutes_played_filter} minutes played', 
        ha='left',
        va='bottom'
    )

    # PL logo
    project_root = Path(__file__).parent.parent
    logo_path = project_root / 'static' / 'pl-logo.png'
    logo = mpimg.imread(logo_path)
    imagebox = OffsetImage(logo, zoom=0.25)
    ab = AnnotationBbox(
        imagebox, 
        (1, 0),                     # location of annotation box
        xycoords='axes fraction',   # use axes fraction coordinates: relative to axes and percentage of axes for position
        box_alignment=(1, 0),       # alignment of the annotation box: (1, 0) means right-aligned and bottom-aligned
        frameon=False               # don't show the frame of the annotation box
    )
    heading_ax.add_artist(ab)

    # Set offset
    offset = 0.01 * df[metric].max()

    # Loop through ranking to plot data, names and metric values
    for i, row in df.iterrows():
        # Plot data
        main_ax.barh(
            row['short_name'], 
            row[metric], 
            color=style_config['colors'][row['role'].lower()],
            alpha=style_config['alpha']
        )

        # Plot player name
        main_ax.text(
            0 - offset, 
            i,
            f"{row['short_name']}", 
            fontproperties=style_config['fonts']['medium'],
            ha='right',
            va='center',
        )

        # Display metric value
        main_ax.text(
            row[metric] - offset, 
            row['short_name'], 
            f"{row[metric]:.3f}", 
            fontproperties=style_config['fonts']['bold'],
            color=style_config['colors']['background'],
            va='center', 
            ha='right', 
        )

    # Set legend text
    xD_text = 'Expected Danger (xD) is a \'danger score\' that tells us how likely a pass is to create a real scoring threat.\nIt\'s calculated by multiplying the probability of a pass leading to a shot with the probability of that shot being a goal.'
    danger_text = 'Danger passes are passes that end in a shot within 15 seconds.\nThese stats are standardized to 90 minutes played to be able to easily compare players with different playing times.'
    legend_text = xD_text if metric == 'xD_per_90' else danger_text
    legend_ax.text(
        0, 
        1, 
        legend_text,
        fontsize=style_config['sizes']['label'], 
        ha='left', 
        va='top'
    )

    return fig