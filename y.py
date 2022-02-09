#yAxis : Median Income
import gzip
import re

#/data/raw/ZipIncome/IncomePop.gz                                         
data = gzip.open("./data2", "rt")

#create a dictionary to collect the median income based on zipcodes
medianIncome = dict()

#read the first line of the data                                                                                                            
line = data.readline()
#loop through each line of the data 
while line:
    #splt the line based on pipe
    fields = line.split("|")
    #load median income data (field2) into the dict with the zip (field 1) as the key     
    medianIncome[fields[0]] = fields[1]
    #get the next 'read line' from the data for the while loop
    line = data.readline()
#when done looping close the file                                                                                                           
data.close()

#for every key in the medianIncome dictionary 
for key in medianIncome:
    #print to standard out the key followed by a pipe followed by string of median income   
    print(key + "|" + str(medianIncome[key]))




