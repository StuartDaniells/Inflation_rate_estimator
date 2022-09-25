# Stuart Daniells
# C0829441
# Final Project
# Inflation rate values from year 1900 to 2022

# Stuart Daniells = SD

# ----------------------------------------------------------------------------
# SD01 on 23rd April: 
# Created random  inflation rate value data, wrote the data to a csv file
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# SD02 on 25rd April: 
# used pandas to read csv data into a list, used mathplotlib to plot the data,
# displaying the max and min values for inflation rate - setsize of 30 years
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# SD03 on 28th April: 
# added custom font family and colours to labels, 
# calculated max overall inflation value from 1900 to 2022,
# used matplotlib annotation to annotate a arrowline and text of overall max,
# added a background grid, set figure size to a larger dimention
# ----------------------------------------------------------------------------


import matplotlib.pyplot as graph
import pandas as panda
import csv
import random

# Didn't find a need to use numpy in this project - since basic python lists sufficed
# import numpy as np

axisHeaders = ['Year', 'Inflation']

inflationData = []

maxInflation = 0
xValueAtyMax = 0 


# setting the figure size for the graph
fig, ax = graph.subplots(figsize=(12, 6))													#SD03


# Generating random inflation rate values between 0 and 10 (inclusive)
for year in range(1900, 2023):																#SD01
    inflationRate = round(random.uniform(0.0, 10.0), 2)
    inflationData.append([year, inflationRate])

# creating InflationDataSheet.csv file and writing to it the random inflation rate values attained
with open('InflationDataSheet.csv', 'w', encoding='UTF8', newline='') as file:				#SD01
    dataInFile = csv.writer(file)	
    dataInFile.writerow(axisHeaders)
    dataInFile.writerows(inflationData)

print("\n--------------------- START -----------------------\n")

# printing the inflation Data of InflationDataSheet.csv file using pandas library
dataInFile = panda.read_csv('InflationDataSheet.csv')										#SD02

# displaying each row value of index, year, inflation value
print(dataInFile)

# getting the shape of the list -> row and coloumn count
rowLength = list(dataInFile.shape)[0]
initialXValue = 0

print("\n--------------------------------------------------")

print("\nThe inflation rates maximum and minimum values are as seen below:\n")

# displaying the year labels on x-axis for every 30 years
for i in range(30, rowLength, 30):															#SD02
    row = dataInFile[initialXValue: i]

    # plotting the graph based on the data, with peak marker as symbol - 'o' and colour black
    graph.plot(row.Year, row.Inflation, label=initialXValue + 1900, marker = 'o', mec = '#000000')
    
    # getting the list form of all inflation rate values
    inflationValueList = list(row.Inflation)

    # Displaying the max and min values
    if len(inflationValueList) > 2:															#SD02
	    print("For years", initialXValue + 1900, "to", i + 1900)
	    print("Max rate =", max(inflationValueList))
	    print("Min rate =", min(inflationValueList))

    print("\n")

    # getting the max inflation value from years 1900 to 2022
    if (maxInflation < max(inflationValueList)):											#SD03
    	maxInflation = max(inflationValueList)
    	# getting the max x-axis (year) value for the corresponding inflation value
    	xValueAtyMax = list(row.Year)[inflationValueList.index(maxInflation)]
    
    initialXValue = i


print("---------------------- END -------------------------")

# creating an arrow pointer, pointing to the max inflation rate from years 1900 to 2022
ax.annotate("Max Value",																	#SD03
            xy=(xValueAtyMax, maxInflation),
            xytext=((xValueAtyMax + 10), (maxInflation + 1.35)),
            size=15, color='black',
            arrowprops=dict(arrowstyle="simple", connectionstyle="arc3,rad=-0.2"))


# Styling of title, xlable and ylabel
font1 = {'family':'serif','color':'blue','size':20}											#SD03
font2 = {'family':'serif','color':'darkred','size':15}

# naming the graph axis lables with custom fonts
graph.title("Rate of Inflation from year 1900 to 2022:", fontdict = font1)					#SD02
graph.xlabel("Year", fontdict = font2)
graph.ylabel("Inflation Rate", fontdict = font2)  # labelling

# displaying a legend info box with the colour for each graph line range
graph.legend()																				#SD02

# setting a green grid in the backgroun with grid lines dotted and thickness as 0.5
graph.grid(color = 'green', linestyle = '--', linewidth = 0.5)								#SD03

# Displaying the graphical data
graph.show()





