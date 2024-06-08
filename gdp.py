import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


gdp_csv = pd.read_csv('gdp-project/all_data.csv')

print(gdp_csv.head)


#distribution of GDP in different countries for all years

sns.barplot(x=gdp_csv.Country, y=gdp_csv.GDP)
plt.xticks(rotation=30, fontsize=8)
plt.legend(['Country', 'GDP'])
plt.show()
plt.clf()


# distribution of GDP for each country

plt.plot(gdp_csv.GDP[gdp_csv.Country == 'Chile'], linestyle='--', marker='o')
plt.xlabel('Distribution of GDP in Chile')
plt.ylabel('GDP')
plt.show()


plt.plot(gdp_csv.GDP[gdp_csv.Country == 'China'], linestyle='--', marker='o')
plt.xlabel('Distribution of GDP in China')
plt.ylabel('GDP')
plt.show()


plt.plot(gdp_csv.GDP[gdp_csv.Country == 'Germany'], linestyle='--', marker='o')
plt.xlabel('Distribution of GDP in Germany')
plt.ylabel('GDP')
plt.show()


plt.plot(gdp_csv.GDP[gdp_csv.Country == 'Mexico'], linestyle='--', marker='o')
plt.xlabel('Distribution of GDP in Mexico')
plt.ylabel('GDP')
plt.show()


plt.plot(gdp_csv.GDP[gdp_csv.Country == 'United States of America'], linestyle='--', marker='o')
plt.xlabel('Distribution of GDP in USA')
plt.ylabel('GDP')
plt.show()


plt.plot(gdp_csv.GDP[gdp_csv.Country == 'Zimbabwe'], linestyle='--', marker='o')
plt.xlabel('Distribution of GDP in Zimbabwe')
plt.ylabel('GDP')
plt.show()


# Different mean GDP in countries

df_gdp_mean = gdp_csv.groupby('Country').GDP.mean().reset_index()

list_gdp_mean = [1.697888e+11, 4.957714e+12, 3.094776e+12, 9.766506e+11, 1.407500e+13]
list_gdp_mean_labels = ['Chile', 'China', 'Germany', 'Mexico', 'USA']
plt.pie(list_gdp_mean, labels=list_gdp_mean_labels)
plt.show()


# Difference between China and Germany

def create_x(t, w, n, d):
    return [t * x + w * n for x in range(d)]


china_gdp = gdp_csv.GDP[gdp_csv.Country == 'China']

germany_gdp = gdp_csv.GDP[gdp_csv.Country == 'Germany']

china_x = create_x(2, 0.8, 1, 16)
germany_x = create_x(2, 0.8, 2, 16)

middle_x = [(a + b) / 2.0 for a,b in zip(china_x, germany_x)]

china_germany_labels = range(2001, 2017)

ax = plt.subplot()

plt.bar(china_x, china_gdp)
plt.bar(germany_x, germany_gdp)
plt.legend(['China', 'Germany'])
plt.xticks(rotation=30)
ax.set_xticks(middle_x)
ax.set_xticklabels(china_germany_labels, )
plt.show()




