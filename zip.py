#Combining based on Zip
import gzip
import re

#open the piple delimited xAxis and yAxis files
xf = open("xAxis", "rt")
yf = open("yAxis", "rt")

#create a first dictionary for the zipcodes and x coordinates
z = dict()
#read the first line of the x file and strip (to remove any leading or trailing spaces and new lines)
line = xf.readline().strip()
#loop through each line of the data 
while line:
    #split on pipe
    fields = line.split("|")
    #set the key to be the zip and the data to be the x coordiante
    z[fields[0]] = fields[1]
    #get the next 'read line' from the data for the while loop and strip
    line = xf.readline().strip()
#when done looping close the file   
xf.close()

#create a second dictionary for the zipcodes and y cooridinates 
z2 = dict()
#read the first line of the y file and strip
line = yf.readline().strip()
#loop through each line of the data  
while line:
    #split on pipe 
    fields = line.split("|")
    #set the key to be the zip and the data to be the y coordiante 
    z2[fields[0]] = fields[1]
    #get the next 'read line' from the data for the while loop and strip
    line = yf.readline().strip()
#when done looping close the file
yf.close()

#make a combination dictionary
comb = dict()
#for every key(zipcode) in the second dictionary
for key in z2:
    #if the key is in the first dictionary
    if key in z:
        #set the key to be the zipcode and set the data to be a list containing its x and y coordinates
        comb[key] = [z[key],z2[key]]

#for every key in the combination dictionary
for key in comb:
    #print the key followed by a pipe followed by the x coord followed by another pipe followed by the y coord
    print(key +  "|" + str(comb[key][0]) + "|" + str(comb[key][1]))
        
