"""
Code to read in, index, and plot a csv file of CTD data.
"""

# imports
import pandas
import matplotlib.pyplot as plt
# names of files to open
csv_fn = '../elahr_data/ctd_data.csv'
# load files int DataFrames
df1 = pandas.read_csv(csv_fn)
#check data header/footer, get col names
print(df1.head)

#plot a subset of the CTD data
plt.scatter(df1['b'], -df1['d'])
plt.title('CTD Data')
plt.xlabel('Temperature (C)')
plt.ylabel('Depth (m)')

plt.show() # Depending on whether you use IPython or interactive mode, etc.
