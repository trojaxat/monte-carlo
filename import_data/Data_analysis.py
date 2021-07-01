import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
# Set figure size to (14,6)
plt.rcParams['figure.figsize'] = (14,6)


# ### Load the data

df=pd.read_csv(f'import_data/data/monday.csv',parse_dates=True, delimiter=';', index_col='timestamp')

all_data=[]
all_days=['monday','tuesday','wednesday','thursday','friday']
for days in all_days:
    all_data.append(pd.read_csv(f'import_data/data/{days}.csv', parse_dates=True, delimiter=';'))
df=pd.concat (all_data, axis=0)

df.shape

df['timestamp']=pd.to_datetime(df['timestamp'])
df['year']=pd.to_datetime(df['timestamp'].astype(str)).dt.year
df['day']=df.timestamp.dt.day_name()
df['hour']=pd.to_datetime(df['timestamp'].astype(str)).dt.hour
df['minute']=pd.to_datetime(df['timestamp'].astype(str)).dt.minute
df

df['hash']=df['customer_no'].astype(str)+df['day']
df


# ### Explore the data

df.head() #checl how it looks
df.shape #check amount of rows and columns
df.info()  ##check the info
df.describe()  #check the mean, min and max and etc 
df.isna().sum() #check the missing values
df.value_counts()   #count the values


# ### Calculate the total number of customers in each section

cust=df['location'].value_counts()          
cust

plt.figure(figsize=(12,7))           #plot the total number of customers in each section
sns.countplot(x='location',data=df)


# ### Calculate the total number of customers in each section over time

customers_dairy=df.loc[df['location']=='dairy'].value_counts()
customers_drinks=df.loc[df['location']=='drinks'].value_counts()
customers_spices=df.loc[df['location']=='spices'].value_counts()
customers_fruit=df.loc[df['location']=='fruit'].value_counts()
customers_checkout=df.loc[df['location']=='checkout'].value_counts()
customers_fruit


#or
df.groupby(['timestamp','location']).customer_no.count()

fig, ax = plt.subplots(figsize=(18,8))
sns.barplot(x='hour', y='customer_no', hue='location', data=df, alpha=0.6).set(title='Total number of customers in each section over time', ylabel='Amount of customers', xlabel= 'Hours')
# the total number of customers in each section over time

#or
df.groupby(['location','hour']).customer_no.count().unstack(0).plot.bar()


#or 
df.groupby('hour')['customer_no'].count().plot.bar()

plt.figure(figsize=(14,6))    
grid = sns.FacetGrid(data=df, col='location',  palette=['#FFAD11'] )   #plot the total number of customers in each section
grid.map_dataframe(sns.countplot, 'hour')                                        
grid.add_legend()                                                        #split the plots by locations
plt.yscale("log")
grid.set_xlabels("Hour")
grid.set_ylabels("Amount of customers")
sns.despine()
plt.show

# ### Display the number of customers at checkout over time

costumers_checkout=df.loc[df['location']=='checkout']
costumers_checkout

sns.barplot(data=costumers_checkout #plot the number of customers in checkout section
             , x='hour', y= 'customer_no')

# ### Calculate the time each customer spent in the market

each_ct=df.groupby('customer_no')['timestamp'].max() - df.groupby('customer_no')['timestamp'].min()
each_ct

#or
# Calculating the amount of time spent by each customer by its last timestamp minus its first timestamp
df.groupby(["day", "customer_no"])["timestamp"].max().unstack().fillna(0) - df.groupby(["day", "customer_no"])["timestamp"].min().unstack().fillna(0)

#or another way would be

df_ct = df.sort_values(by=['customer_no', 'timestamp'])
df_ct.loc[df_ct['customer_no'] ==
              15]['timestamp'].iloc[0]  # example to check it works
df_ct.loc[df_ct['customer_no'] ==
              15]['timestamp'].iloc[-1]  # example to check it works

df_customer = pd.DataFrame(
    data=None, columns=['customer_no', 'time_taken'], dtype=None, copy=False)
df_customer['customer_no'] = df['customer_no']
df_customer

times = []
for customer_number in df_ct['customer_no'].unique():
    time_value = df_ct.loc[df_ct['customer_no'] == customer_number]['timestamp'].iloc[-1] -         df_ct.loc[df_ct['customer_no'] ==
                      customer_number]['timestamp'].iloc[0]
    times.append(time_value)
    df_customer['time_taken'] = time_value
test = list(zip(df_ct['customer_no'].unique(), times))

df_customer['time_taken'] = df_ct.groupby('customer_no')['timestamp'].max(
) - df_ct.groupby('customer_no')['timestamp'].min()
df_customer

df_ct.groupby('customer_no')['timestamp'].max(
) - df_ct.groupby('customer_no')['timestamp'].min()

df.loc[df['customer_no'] == df_customer['customer_no']].index[0]
df.loc[(1 == df['customer_no']) & (df['location'] == 'checkout')]

df_customer = df_customer.dropna()
df_customer.info()

sns.countplot(y="customer_no", data=df_customer)   #plot the time taken
plt.show()

(df_customer['time_taken'].astype('timedelta64[s]') / 60).plot.hist() #plot time taken
plt.show()

# ### Calculate the total number of customers in the supermarket over time.

df.groupby('timestamp').customer_no.count()

df.groupby('hour')['customer_no'].count().plot.bar()


# ### Our business managers think that the first section customers visit follows a different pattern than the following ones. Plot the distribution of customers of their first visited section versus following sections (treat all sections visited after the first as “following”).

df = df.sort_values(by=['hash', 'timestamp'])
df

df["order"] = None
for i in range(len(df)):
    if df["hash"].iloc[i] != df["hash"].iloc[i-1]:
        df["order"].iloc[i] = "first"
    else:
        df["order"].iloc[i] = "following"


df.head(10)

#ploting the Total count of bikes rented duriung each hour (per day)
fig, ax = plt.subplots(figsize=(15,6))
sns.barplot(x='hour', y='location', hue='order', data=df, alpha=0.6).set(title='The sections visited first and following times', ylabel='Sections', xlabel= 'Hours')

##checking how the behaviour of customers change over the days (separate plots for each weekday)
g= sns.FacetGrid(df, col='day')
g.map(sns.histplot,'order')
plt.yscale("log")
plt.show

df.groupby(['order','day']).order.count().unstack(0).plot.bar() 
##checking how the behaviour of customers change over the days

#closer look at the customer behaviour over weekday,hours and sections
fig,(ax1,ax2,ax3) = plt.subplots(ncols=3)
fig.set_size_inches(16, 8)
sns.barplot(x="hour", y="customer_no", hue='order', data=df,ax=ax1,color='r')
sns.barplot(x="day",  y="customer_no", hue='order', data=df,ax=ax2, color='g')
sns.barplot(x="location", y="customer_no", hue='order', data=df,ax=ax3)

# ### Estimate the total revenue for a customer using the following table:

df1 = pd.DataFrame({
    'section': ['fruit', 'spices', 'dairy', 'drinks'],
    'revenue per minute in Euros(€)': [4, 3, 5, 6]
    })
df1

# #### Which is the most profitable section according to your data?

df

min_s=df['minute'].sum()          #sum uo the minutes to calculate the revenue per minute afterwards
min_s


hour_s=df['hour'].sum()          #sum uo the minutes to calculate the revenue per minute afterwards
hour_s

min_pm=df1['revenue per minute in Euros(€)']*min_s
min_pm

df1['revenue per minute']=min_pm  #add a column of a revenue per minute
df1

df1.max()    #finding the most profitable section according to our data?
#according to the data the most profitable section is spices

hour_pm=df1['revenue per minute in Euros(€)']*hour_s      #check the numbers in hours 
hour_pm

df1['revenue per hour']=hour_pm     #add a column of a revenue per hour
df1 

df1['revenue per hour'].max()    #finding the most profitable section according to our data?