import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('import_data/data/monday.csv', parse_dates=True,
                 delimiter=';', index_col='timestamp')

all_data = []
all_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
for days in all_days:
    all_data.append(pd.read_csv(
        f'import_data/data/{days}.csv',                    parse_dates=True, delimiter=';'))

big_df = pd.concat(all_data, axis=0)
big_df['timestamp'] = pd.to_datetime(big_df['timestamp'])
big_df['day'] = big_df.timestamp.dt.day_name()
big_df['hashed_index'] = big_df['day'].astype(
    'str') + big_df.customer_no.astype('str')

df.shape
df.describe()
df.info()

customers = df.groupby(["location"]).sum()
df.groupby(["location"]).sum().plot()

# Calculate the total number of customers in each section
plt.figure(figsize=(12, 7))
sns.countplot(x="location", data=df)
plt.show()

# Calculate the total number of customers in each section over time
df.index = pd.to_datetime(df.index)
df['hour'] = [x.hour for x in df.index]  # Add hour as column
df['day'] = [x.day for x in df.index]  # Add hour as column

plt.figure(figsize=(12, 7))
subset = df.drop(df[df['location'] == 'checkout'].index)
sns.lineplot(x="hour", y="customer_no", hue="location", data=subset)
plt.show()

# Display the density of customers at a specific place over time
plt.figure(figsize=(12, 7))
selection = ['dairy', 'drink', 'fruit', 'spices']
for option in selection:
    newDf = df.loc[df['location'] == option]
    sns.distplot(newDf['customer_no'], hist=True, kde=True)
plt.show()

# Display the number of customers at checkout over time
plt.figure(figsize=(12, 7))
newDf = df.loc[df['location'] == 'checkout']
sns.regplot(y="customer_no", x="hour", data=newDf,
            color='k', scatter_kws={"alpha": 0.0})
# sns.swarmplot(y="customer_no", x="hour",data= newDf)
# if they are both on, Since swarmplot is a categorical plot,
# the axis in the plot still goes from -0.5 to 8.5 and not as the labels suggest from 10 to 18.
plt.show()

fig, ax = plt.subplots()
ax2 = ax.twiny()
sns.swarmplot(y="customer_no", x="hour", data=newDf, ax=ax)
sns.regplot(y="customer_no", x="hour", data=newDf,
            color='k', scatter_kws={"alpha": 0.0},  ax=ax2)
ax2.grid(False)
plt.show()

# Calculate the time each customer spent in the market
df = df.reset_index('timestamp')
df_sorted = df.sort_values(by=['customer_no', 'timestamp'])
df_sorted.loc[df_sorted['customer_no'] ==
              15]['timestamp'].iloc[0]  # example to check it works
df_sorted.loc[df_sorted['customer_no'] ==
              15]['timestamp'].iloc[-1]  # example to check it works

df_customer = pd.DataFrame(
    data=None, columns=['customer_no', 'time_taken'], dtype=None, copy=False)
df_customer['customer_no'] = df['customer_no']
df_customer

times = []
for customer_number in df_sorted['customer_no'].unique():
    time_value = df_sorted.loc[df_sorted['customer_no'] == customer_number]['timestamp'].iloc[-1] - \
        df_sorted.loc[df_sorted['customer_no'] ==
                      customer_number]['timestamp'].iloc[0]
    times.append(time_value)
    df_customer['time_taken'] = time_value
test = list(zip(df_sorted['customer_no'].unique(), times))

df_customer['time_taken'] = df_sorted.groupby('customer_no')['timestamp'].max(
) - df_sorted.groupby('customer_no')['timestamp'].min()
df_customer

df_sorted.groupby('customer_no')['timestamp'].max(
) - df_sorted.groupby('customer_no')['timestamp'].min()

df.loc[df['customer_no'] == df_customer['customer_no']].index[0]
df.loc[(1 == df['customer_no']) & (df['location'] == 'checkout')]

df_customer = df_customer.dropna()
df_customer.info()

sns.countplot(y="customer_no", data=df_customer)
plt.show()

(df_customer['time_taken'].astype('timedelta64[s]') / 60).plot.hist()
plt.show()

# Calculate the total number of customers in the supermarket over time.
sns.barplot(y="customer_no", x='hour', data=df)
plt.show()

plt.figure(figsize=(12, 7))
grid = sns.FacetGrid(data=df, col='location',  palette=['#FFAD11'])
grid.map_dataframe(sns.countplot, 'hour')
grid.add_legend()
plt.yscale("log")
grid.set_xlabels("Hour")
grid.set_ylabels("Amount of customers")
sns.despine()
plt.show()


fig, ax = plt.subplots(figsize=(15, 6))
sns.barplot(x='location', y='customer_no', hue='day', data=df, alpha=0.6).set(
    title='Total count of customers in each sections over the time', ylabel='Amount customers', xlabel='Hours')
plt.show()

# Our business managers think that the first section customers visit follows a different pattern than the following
# ones. Plot the distribution of customers of their first visited section versus following sections (
# treat all sections visited after the first as “following”
