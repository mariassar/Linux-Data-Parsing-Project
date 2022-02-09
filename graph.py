import matplotlib.pyplot as plt

#create a figure instance that will later be written to a PDF
f = plt.figure()

#open zip file
zipf = open("zip", "rt")
#create a dictionary for x coords
xCoords = []
#create a dictionary for y coords
yCoords = []

#read the first line of the file and strip
line = zipf.readline().strip()
#loop through each line of the data 
while line:
    #spilt on pipe
    fields = line.split("|")
    #load in the x coord
    xCoords += [float(fields[1])]
    #load in the y coord
    yCoords += [int(fields[2])]
    #get the next 'read line' from the data for the while loop and strip
    line = zipf.readline().strip()
#when done looping close the file 
zipf.close()

#create the scatterplot with the x and y coord dictionaries
plt.scatter(xCoords, yCoords)

#specify title , x axis, and y axis
plt.title("The Likelihood of Death After a 911 Call in a NY Poor Nei\
ghborhood is More Than in a NY Rich Neighborhood (2006-2010).",fontsize=5.5)    
plt.xlabel("Death Ratio")
plt.ylabel("Median Income")

#save the plot into a PDF file
f.savefig("graph.pdf")
