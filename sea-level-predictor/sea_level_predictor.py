import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    full_reg = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    full_x = pd.Series(range(1880, 2051))
    full_y = full_reg.slope * full_x + full_reg.intercept
    ax.plot(full_x, full_y, label="Full Fit", color="red")


    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    recent_reg = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    recent_x = pd.Series(range(2000, 2051))
    recent_y = recent_reg.slope * recent_x + recent_reg.intercept
    ax.plot(recent_x, recent_y, label="Since 2000", color="green")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()