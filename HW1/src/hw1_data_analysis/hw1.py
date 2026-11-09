#1: Import pandas and read the csv file into a pandas dataframe.
import pandas as pd
df = pd.read_csv('bicycle_data.csv')
print(df.head())

#2: Updating to prper data types.
column_list = df.columns.tolist()
print(column_list)
print(df.dtypes)
#the columns are the time, the number of bicycles for the West and East Sidewalks 
#and the total number of bicycles on the bridge sidewalks.
#I expect the time as a string, and the number of bicycles as integers.
#The original data type in this file is string for time and float for the number. 
#We need to convert the data type for the number of bicycles from floats to intergers.
column_update = column_list[1:4]
df[column_update] = df[column_update].astype("Int64")
print(df.dtypes)

#3: Add additional columns to data
East_bi = df[column_update[1]]
West_bi = df[column_update[2]]
total_bi = East_bi + West_bi
#Add total count of East + West column
df['Total Bicycles (East + West)'] = total_bi
date_time_list_raw = df[column_list[0]]
date_time_list = date_time_list_raw.str.split(' ')
print(date_time_list)
date_list = [date_time_list[i][0] for i in range(len(date_time_list))]
time = [date_time_list[i][1] for i in range(len(date_time_list))]
AM_PM_list = [date_time_list[i][2] for i in range(len(date_time_list))]
time_list = [time[i] + ' ' + AM_PM_list[i] for i in range(len(time))]
print(time_list)
#Add hour of the day column
df['hour of the day'] = time_list
date_split = [date_list[i].split('/') for i in range(len(date_list))]
year_list = [date_split[i][2] for i in range(len(date_split))]
#Add year column
df['year'] = year_list
print(year_list)

#4: Sebset df for year 2016
index_list = [i for i in range(len(year_list)) if year_list[i] == '2016']
sub_df = df.iloc[index_list, [0,1,2,3,4,5,6]]
print(sub_df.head())              

#5: Check for missing values 
print(sub_df.isna().any())
#Check the number of missing data
print(sub_df.isna().sum())
#After running the code, we can see that there is 1 point of missing data
#in all of the three columns for the number of bicucles. We can remove these empty rows.
#Remove the rows with missing data
sub_df = sub_df.dropna()

#6: Plot Hour of the Day VS Total Counts and save the image
#Sort by the values of the time_list
subdf_sorted = sub_df.sort_values(by='hour of the day')
#Group the total numbers of bicycles for the same hour of the day
subdf_grouped = subdf_sorted.groupby('hour of the day')['Total Bicycles (East + West)'].sum().reset_index()
print(subdf_grouped)
#Plot the data
import matplotlib.pyplot as plt
group_column = subdf_grouped.columns.tolist()
print(group_column)
print(subdf_grouped.shape)
plt.figure(figsize=(10, 8))
plt.title('Hour of the Day VS 2016 Total Counts', fontsize=16, fontweight='bold')
plt.xlabel('Hour of the Day',fontsize = 14)
plt.ylabel('Total Counts of Bicycles',fontsize = 14)
x_ticks_raw  = subdf_grouped[group_column[0]].tolist()
x_ticks = [x_ticks_raw[i][:2] + ' ' + x_ticks_raw[i][-2:] for i in range(len(x_ticks_raw))]
#print(x_ticks)
plt.xticks(rotation = 90)
plt.scatter(x_ticks, subdf_grouped[group_column[1]])
plt.savefig('counts_by_hour.png')
plt.show()

#7: Find the average busiest hour of the day
total_counts = subdf_grouped[group_column[1]].tolist()
max_value = max(total_counts)
max_index = total_counts.index(max_value)
#print(max_index)
bus_hour = x_ticks[max_index]
print(bus_hour)
#From the output, we can see that the Busiest hour of the day is 5PM.

