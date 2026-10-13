import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from utils.plotting import ACCENT, PL_DIVERGING, PRIMARY, SECONDARY, style_plot


def corr_heatmap_plot(
    corr_df: pd.DataFrame,
    title: str,
    fig_size: tuple[int, int] = (18, 14),
    annot: bool = False,
) -> None:
    """Plot a correlation matrix as a styled heatmap.

    Used for visualizing relationships across a full or category-level set
    of features. Uses a fixed -1 to 1 colour scale so correlation strength
    is comparable across different heatmaps.

    Parameters
    ----------
    corr_df : pd.DataFrame
        A correlation matrix (e.g. from `df.corr()`), signed — not the
        absolute-value version, since sign is needed for correct
        interpretation of the heatmap colours.
    title : str
        Title displayed above the heatmap.
    fig_size : tuple[int, int], default (18, 14)
        Figure size in inches.
    annot : bool, default False
        Whether to display correlation values on each cell. Recommended
        False for large matrices (unreadable) and True for small, curated
        feature subsets.

    Returns
    -------
    None
        Displays the plot; does not return the figure or axes.
    """

    fig, ax = plt.subplots(figsize=fig_size)

    sns.heatmap(
        corr_df,
        cmap=PL_DIVERGING,
        center=0,
        vmin=-1,
        vmax=1,
        annot=annot,
        linewidths=0.4,
        linecolor="white",
        square=False,
        cbar_kws={
            "orientation": "horizontal",
            "shrink": 0.5,
            "pad": 0.1,
            "label": "Correlation",
        },
        ax=ax,
    )

    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, fontsize=10, ha="right")
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=11, ha="right")

    style_plot(
        ax=ax,
        title=title,
    )

    plt.tight_layout()
    plt.show()


def investigate_correlation_pair(
    df: pd.DataFrame,
    feature_pair: tuple[str, str],
    corr_table: pd.DataFrame | None = None,
) -> None:
    """Plot distributions and a scatter plot for a pair of features, annotated
    with Pearson and Spearman correlation.

    Used to visually investigate feature pairs flagged as near-duplicates or
    strongly correlated during feature screening.

    Parameters
    ----------
    df : pd.DataFrame
        Source dataframe containing both features as columns.
    feature_pair : tuple[str, str]
        The two column names to compare, e.g. ("shots", "np_shots").
    corr_table : pd.DataFrame, optional
        Precomputed correlation table to look up values from, avoiding
        recomputation and keeping plotted values consistent with prior
        analysis. Must contain columns: "Feature 1", "Feature 2",
        "correlation_pearson", "correlation_spearman". The pair is matched
        in either column order. If None, Pearson and Spearman correlation
        are computed directly from `df` for just this pair.

    Returns
    -------
    None
        Displays the plot; does not return the figure or axes.
    """

    feature_1, feature_2 = feature_pair

    if corr_table is not None:
        match = corr_table[
            (
                (corr_table["Feature 1"] == feature_1)
                & (corr_table["Feature 2"] == feature_2)
            )
            | (
                (corr_table["Feature 1"] == feature_2)
                & (corr_table["Feature 2"] == feature_1)
            )
        ]
        row = match.iloc[0]
        pearson, spearman = row["correlation_pearson"], row["correlation_spearman"]
    else:
        pearson = df[feature_1].corr(df[feature_2], method="pearson")
        spearman = df[feature_1].corr(df[feature_2], method="spearman")

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    axes[0].hist(df[feature_1], bins=20, color=ACCENT, edgecolor=PRIMARY, alpha=0.85)
    axes[0].set_title(feature_1, fontsize=10, color=PRIMARY)

    axes[1].hist(df[feature_2], bins=20, color=SECONDARY, edgecolor=PRIMARY, alpha=0.85)
    axes[1].set_title(feature_2, fontsize=10, color=PRIMARY)

    axes[2].scatter(
        df[feature_1],
        df[feature_2],
        color=ACCENT,
        edgecolor=PRIMARY,
        linewidth=0.6,
        s=50,
        alpha=0.85,
    )
    axes[2].set_title(f"r={pearson:.2f} (ρ={spearman:.2f})", fontsize=10, color=PRIMARY)
    axes[2].set_xlabel(feature_1, fontsize=8)
    axes[2].set_ylabel(feature_2, fontsize=8)

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(labelsize=7)

    fig.suptitle(
        f"{feature_1} vs {feature_2}  (n={len(df)})",
        fontsize=13,
        fontweight="bold",
        color=PRIMARY,
        y=1.03,
    )
    plt.tight_layout()
    plt.show()
