import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import os

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("C:/Users/pixel/Python_codding/Freecodecamp_data_science/Final_projects/final_time_series_visualizer/fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
df = df.loc[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    fig, axs = plt.subplots(figsize=(32, 10), squeeze=True)
    fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    axs.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize=18)
    axs.set_ylabel("Page Views", fontsize=18)
    axs.set_xlabel("Date", fontsize=18)
    axs.tick_params(labelsize=18)
    axs.plot(df, color="red", linewidth=2)

    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    df_bar = df.reset_index()
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month_name()
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=months, ordered=True)
    df_bar.drop('date', axis=1, inplace=True)
    df_bar = df_bar.groupby(['year', 'month']).mean().unstack(level=-1)

    # Draw bar plot
    fig = df_bar.plot(kind='bar', figsize=(10, 8)).figure
    plt.legend(months, fontsize=14)
    plt.xlabel('Years', fontsize=13)
    plt.ylabel('Average Page Views', fontsize=13)
    plt.tick_params(labelsize=12)


    # Save image and return fig (don't change this part)
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Draw box plots (using Seaborn)

    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig
