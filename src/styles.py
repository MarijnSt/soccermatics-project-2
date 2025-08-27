from pathlib import Path
from matplotlib import font_manager

# Get the directory where this script is located
script_dir = Path(__file__).parent
# Go up one level to project root, then into assets
font_path = script_dir.parent / 'assets' / 'Futura.ttc'

# Load font
font_manager.fontManager.addfont(str(font_path))
prop = font_manager.FontProperties(fname=str(font_path))

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
    'font_prop': prop
}