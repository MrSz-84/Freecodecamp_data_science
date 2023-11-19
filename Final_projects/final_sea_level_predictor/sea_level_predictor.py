import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('C:/Users/pixel/Python_codding/Freecodecamp_data_science/Final_projects/final_sea_level_predictor/epa-sea-level.csv')
    df_short = df.loc[df['Year'] >= 2000]
    reg_long = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    reg_short = linregress(df_short['Year'], df_short['CSIRO Adjusted Sea Level'])
    extended_years = pd.Series([y for y in range(1880, 2051, 1)])
    extended_years_short = pd.Series([y for y in range(2000, 2051, 1)])
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.3, color='purple')

    # Create first line of best fit
    plt.plot(extended_years, reg_long.intercept + reg_long.slope * extended_years, 'r', alpha=0.5)

    # Create second line of best fit
    plt.plot(extended_years_short, reg_short.intercept + reg_short.slope * extended_years_short, 'green', alpha=0.7)

    # Add labels and title
    ax.set_ylabel('Sea Level (inches)')
    ax.set_xlabel('Year')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()