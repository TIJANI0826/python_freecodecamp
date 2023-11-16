import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = df.plot(kind='line', figsize=(16,10))




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    calendar = df_bar.index.month
    df_bar['month'] = df_bar['month'].apply(lambda x: calendar.month_abbr[x])
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Draw bar plot
    fig = df_bar.plot(kind='bar', figsize=(12, 10))
    plt.xlabel('Year')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=calendar.month_abbr[1:])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig = sns.boxplot(x='year', y='value', data=df_box, palette='Set2')  

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
