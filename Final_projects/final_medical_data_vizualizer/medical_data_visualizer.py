import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('C:/Users/pixel/Python_codding/Freecodecamp_data_science/final_medical_data_vizualizer/medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df[['weight', 'height']].apply(lambda x: 1 if (x[0] / (x[1]/100)**2) > 25 else 0, axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat.columns = ['cardio', 'variable', 'value', 'counts']

    # Draw the catplot with 'sns.catplot()'
    cat_plot = sns.catplot(data=df_cat, x='variable', y='counts', hue='value', kind='bar', height=6, col='cardio')
    cat_plot.set_axis_labels("variable", 'total')


    # Get the figure for the output
    fig = cat_plot


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[(df['ap_hi'] >= df['ap_lo']) 
                 & (df['height'] >= df['height'].quantile(0.025))
                 & (df['height'] <= df['height'].quantile(0.975))
                 & (df['weight'] >= df['weight'].quantile(0.025))
                 & (df['weight'] <= df['weight'].quantile(0.975))
                ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype='bool'))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt='.1f', linewidth=0.7, mask=mask, cbar_kws={"shrink":.5}, center=0.08, square=True, robust=True, ax=ax)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

