from pathlib import Path
from matplotlib import font_manager

# Get the directory where this script is located
script_dir = Path(__file__).parent

# Set font paths
font_path = script_dir.parent / 'assets' / 'Futura.ttc'
font_light_path = script_dir.parent / 'assets' / 'Futura-light.ttf'

# Load font
font_manager.fontManager.addfont(str(font_path))
font_manager.fontManager.addfont(str(font_light_path))

# Create font properties
prop = font_manager.FontProperties(fname=str(font_path))
prop_light = font_manager.FontProperties(fname=str(font_light_path))

# Create style config
style_config = {
    'colors': {
        'background': '#f2f4ee',
        'dark': '#053225',
        'general_stats': '#DC851F',
        'dribble_stats': '#6D98BA',
        'danger_dribble_stats': '#CA2E55',
    },
    'sizes': {
        'h1': 18,
        'h2': 16,
        'h3': 14,
        'p': 12,
        'label': 8,
    },
    'alpha': 0.4,
    'font_prop': prop,
    'font_prop_light': prop_light
}