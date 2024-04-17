# a322_electricity_trends.py
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs 

import matplotlib.pyplot as plt
import pandas as pd

# choose countries of interest
my_countries = ['Afghanistan', 'Dominican Republic', 'Malaysia', 'Zimbabwe']
naandsacountries = ['Mexico', 'Ecuador', 'Brazil', 'Argentina','Canada', 'United States']
EU_Countries = ['Portugal', 'Belgium', 'United Kingdom', 'Italy','Russia', 'France']
ASIA_Countries = ['China', 'Japan', 'Thailand', 'Indonesia','Singapore', 'Vietnam']
AFRICA_Countries = ['Angola', 'Nigeria', 'Ghana', 'Morocco','Egypt', 'Algeria']


# Load in the data with read_csv()
df = pd.read_csv("elec_access_data.csv", header=0)    # header=0 means there is a header in row 0

# get a list unique countries
unique_countries = df['Entity'].unique()

# Plot the data on a line graph
for c in unique_countries:
  if c in my_countries:
    
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == c]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == c]['Access']

    plt.plot(years, sum_elec, label=c, marker='>', linestyle='--')

  
plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()

for o in unique_countries:
  if o in naandsacountries:
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == o]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == o]['Access']

    plt.plot(years, sum_elec, label=o, marker='>', linestyle='--')

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Comparison of 6 NA and SA Countries')
plt.legend()
plt.show()


for a in unique_countries:
  if a in EU_Countries:
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == a]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == a]['Access']

    plt.plot(years, sum_elec, label=a, marker='>', linestyle='--')

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Comparison of 6 EU Countries')
plt.legend()
plt.show()

for q in unique_countries:
  if q in ASIA_Countries:
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == q]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == q]['Access']

    plt.plot(years, sum_elec, label=q, marker='>', linestyle='--')

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Comparison of 6 Asian Countries')
plt.legend()
plt.show()

for y in unique_countries:
  if y in AFRICA_Countries:
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == y]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == y]['Access']

    plt.plot(years, sum_elec, label=y, marker='>', linestyle='--')

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Comparison of 6 African Countries')
plt.legend()
plt.show()