import pandas as pd
import matplotlib.pyplot as plt

# Read in dataset and create appropriate dataframe
df = pd.read_csv("2017-hubway-tripdata_CLEAN.csv")

# 1) Rider distribution
# # Male vs. Female
gender_counts = df['gender'].value_counts().sort_index()
gender_labels = ['Unknown', 'Male', 'Female']
colors = ['yellow', 'blue', 'pink']

fig = plt.figure(figsize=(14,7))
fig.suptitle("Rider Distribution")
plt.subplot(1, 3, 1)
plt.title('Male vs. Female')
plt.pie(gender_counts, labels=gender_labels, colors=colors, autopct='%1.1f%%')
plt.axis('equal')

# # Customer vs. Subscribers
user_counts = df['usertype'].value_counts()
user_labels = ['Subscriber', 'Customer']
colors = ['Green', 'Yellow']

plt.subplot(1, 3, 3)
plt.title('Customers vs. Subscribers')
plt.pie(user_counts, labels=user_labels, colors=colors, autopct='%1.1f%%')
plt.axis('equal')

plt.savefig('Rider_Distribution.png')

# 2) Individual bike usage
# # Find top n most used bikes
n = 10
df_top_10 = df.groupby(['bikeid'])['bikeid'].agg(
    {"count": len}).sort_values("count", ascending=False).head(n).reset_index()

plt.figure()
ax = df_top_10.plot(kind='bar', x='bikeid', y='count', legend=False, title='Top 10 Used Bikes')
ax.set_xlabel('Bike ID')
ax.set_ylabel('Specific Bike Rentals / Year')
plt.savefig('Bike_Usage.png')

# 3) Specific datetime usage
# # Extract the datetime object
temp = pd.DatetimeIndex(df['starttime'])
df['start_date'] = pd.to_datetime(temp.date, format='%Y-%m-%d')
df['start_time'] = pd.to_datetime(temp.time, format='%H:%M:%S')

# # Month of year
month_counts = df['start_date'].groupby([df.start_date.dt.month]).agg('count')

fig = plt.figure(figsize=(14, 7))
fig.suptitle("Specific DateTime Usage")
plt.subplot(1, 2, 1)
ax1 = month_counts.plot(kind='bar', title='Total Rentals / Month')
ax1.set_xlabel('Month of Year')
ax1.set_ylabel('Bike Rentals')

# # Time of day
time_counts = df['start_time'].groupby([df.start_time.dt.hour]).agg('count')

plt.subplot(1, 2, 2)
ax2 = time_counts.plot(kind='bar', title='Total Rentals by Hour')
ax2.set_xlabel('Hour of Day (24hr)')
ax2.set_ylabel('Bike Rentals')
plt.savefig('Specific_DateTime_Usage.png')
