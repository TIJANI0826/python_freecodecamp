import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  
  # Create scatter plot
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
  
  # Create first line of best fit
  slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  plt.plot(df['Year'], slope*df['Year'] + intercept, 'r', label='fitted line 1')  

  # Create second line of best fit
  
  slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  plt.plot(df['Year'], slope2*df['Year'] + intercept2, 'g', label='fitted line 2')
  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
    
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
