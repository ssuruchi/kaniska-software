import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gdp_csv.csv')
y = df['Value']
x = df['Year']
label = df['Country Name']

# Pie Chart
plt.pie(y, labels = x, autopct = '%1.1f%%')
# Bar Chart
plt.bar(x,y, label = label, color = 'g')
# Scatter Plot
plt.scatter(x,y, label = label, color = 'g', marker = '*', s = 30)
# Line Plot
plt.plot(x,y, label = label)

# plt.hist(x, bins = 57, histtype = 'bar')
plt.xticks(np.arange(1960,2016,5))
plt.xlabel('Year')
plt.xlabel('GDP')
plt.title('GDP of India')

year = int(input("Enter the year: "))
try:
    if year > 2022 or year < 1960: 
        raise NameError("Hello")
    else:
        gdp = df[df['Year'] == year]
        print(gdp)
except NameError:
    print("Invalid Year (1960 - 2022)!")
finally:
    print("Query Executed Successfully!")


import seaborn as sns

sns.displot(df['Value'], kde=True)

sns.boxplot(x=df['Value'])