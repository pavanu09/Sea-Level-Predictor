import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    result = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    result2 = linregress(x=df["Year"][df["Year"] >= 2000], y=df["CSIRO Adjusted Sea Level"][df["Year"] >= 2000])
    span = np.arange(1880, 2051, dtype='float64')
    span2 = np.arange(2000, 2051, dtype='float64')


    # Create scatter plot
    fig, ax = plt.subplots(ncols=1, figsize=(10, 10))
    x1 = df.plot.scatter(x="Year", y="CSIRO Adjusted Sea Level", color="b", ax=ax).set(ylabel="Sea Level (inches)", title="Rise in Sea Level")


    # Create first line of best fit
    ax2 = ax.plot(span, result.intercept+result.slope*span, "r")
    # ax3 = df.plot.scatter(x="Year", y="NOAA Adjusted Sea Level", color="r", ax=ax).set(ylabel="Sea Level (inches)")


    # Create second line of best fit
    ax4 = ax.plot(span2, result2.intercept+result2.slope*span2, "y")

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
