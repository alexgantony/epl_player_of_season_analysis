import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

# ======================================================
# Project Color Palette
# ======================================================

PRIMARY = "#37003C"  # Premier League Purple
SECONDARY = "#00FF85"  # Premier League Green
ACCENT = "#FF2882"  # Premier League Pink
MEAN_COLOR = "#1f77b4"
MEDIAN_COLOR = "#d62728"

# ======================================================
# Colormaps
# ======================================================

# Diverging: for correlation heatmaps, anything centered on 0
PL_DIVERGING = mcolors.LinearSegmentedColormap.from_list(
    "pl_diverging", [ACCENT, "#F5F5F5", PRIMARY]
)

# Sequential: for magnitude-only heatmaps (no negative values, e.g. raw stats)
PL_SEQUENTIAL = mcolors.LinearSegmentedColormap.from_list(
    "pl_sequential", ["#F5F5F5", PRIMARY]
)


# ======================================================
# Matplotlib Theme
# ======================================================


def set_plot_theme():
    """Apply the project's default Matplotlib theme."""
    plt.rcParams.update(
        {
            "figure.figsize": (10, 6),
            "figure.dpi": 150,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": "#333333",
            "axes.grid": True,
            "axes.axisbelow": True,
            "grid.color": "#DDDDDD",
            "grid.linestyle": "--",
            "grid.linewidth": 0.6,
            "axes.titlesize": 18,
            "axes.titleweight": "bold",
            "axes.labelsize": 13,
            "xtick.labelsize": 11,
            "ytick.labelsize": 11,
            "legend.fontsize": 11,
            "font.family": "DejaVu Sans",
        }
    )


# ======================================================
# Plot Styling Helpers
# ======================================================


def style_plot(ax, title=None, xlabel=None, ylabel=None):
    """Apply consistent styling to a Matplotlib axis."""

    ax.set_title(title, fontsize=15, fontweight="bold", pad=20, color=PRIMARY)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.grid(axis="y", linestyle="--", alpha=0.4)


# ======================================================
# Constant Variables
# ======================================================

HIST_BINS = 15


# ======================================================
# Highligt Colors
# ======================================================
HIGHLIGHT_HIGH = SECONDARY
HIGHLIGHT_LOW = ACCENT
NEUTRAL = "#B0AEB3"
