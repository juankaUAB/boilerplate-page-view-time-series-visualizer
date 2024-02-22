import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=0, parse_dates=['date'])

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(q=0.025)) & (df['value'] <= df['value'].quantile(q=0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    ax.plot(df.index.date.tolist(), df['value'])
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([(df.index.year), (df.index.month)]).mean()

    # Draw bar plot
    
    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    ax = df_bar.unstack().plot(kind='bar')
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(Months)
    fig = ax.get_figure()

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

    Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, ax = plt.subplots(1, 2, figsize=(15, 4))
    sns.boxplot(y="value", x= "year", data=df_box,  orient='v' , ax=ax[0])
    sns.boxplot(y="value", x= "month", data=df_box,  orient='v' , ax=ax[1], order=Months)
    ax[0].title.set_text('Year-wise Box Plot (Trend)')
    ax[1].title.set_text('Month-wise Box Plot (Seasonality)')
    ax[0].set(xlabel="Year",ylabel="Page Views")
    ax[1].set(xlabel="Month",ylabel="Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
