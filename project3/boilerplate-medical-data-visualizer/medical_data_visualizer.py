import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
BMI = (df['weight']) / (df['height'] ** 2)

df['overweight'] = pd.Series([1 if i > 25 else 0 for i in BMI])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['cholesterol'] = pd.Series([1 if i > 1 else 0 for i in df['cholesterol']]) 
df['gluc'] = pd.Series([1 if i > 1 else 0 for i in df['gluc']])

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars=["cardio"],value_vars = ['active','alco','cholesterol','gluc','overweight','smoke'])
    df_catOne = pd.melt(df,id_vars=["cardio"],value_vars = ['active','alco','cholesterol','gluc','overweight','smoke'])



#     # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
#     df_cat0 = pd.DataFrame(df_cat.groupby('cardio').get_group(0))
#     df_cat1 = pd.DataFrame(df_cat.groupby('cardio').get_group(1)) 
#     df_cat = pd.concat([df_cat0,df_cat1])
#     df_cat = pd.DataFrame(df_cat.value_counts())
    df_cat.reset_index(inplace=True)
    df_cat = df_cat.rename(columns={0: "total"},inplace=True)
    

    # Draw the catplot with 'sns.catplot.show()
    #sns.catplot(y="total",x="variable",hue="value",data=df_cat,kind="bar",col="cardio")

    # Get the figure for the output
    
    sns_plot = sns.catplot(x="variable",hue="value",data=df_catOne,kind="count",col="cardio")
    sns_plot.set_ylabels("total")
    fig =  sns_plot.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] >= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] >= df['weight'].quantile(0.975))]


    # Calculate the correlation matrix
    corr = df_heat.corr().round(2)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr,dtype=bool))

    # Set up the matplotlib figure
    #Create a figure and one subplot

    fig, ax = plt.subplots(figsize=[7.6,8.4],dpi=200,facecolor="cyan",edgecolor="green",layout="constrained") 
    
    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag')
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig