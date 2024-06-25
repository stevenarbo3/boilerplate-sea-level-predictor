import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    df.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level')


    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    extended_years = pd.Series(range(df['Year'].min(), 2051))
    plt.plot(extended_years, res.intercept + res.slope*extended_years, 'r')
    

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    res = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    
    extended_years_2000 = pd.Series(range(2000, 2051))
    plt.plot(extended_years_2000, res.intercept + res.slope*extended_years_2000, 'g')

    # Add labels and title
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()