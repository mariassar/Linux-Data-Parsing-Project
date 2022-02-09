#xAxis: Death Ratio
import gzip
import re

#open symbolic link pointing to EMS Incdent Data
data = gzip.open("./data1", "rt")

#get death ratio numerator and denominator  

#for the denominator: create a dictionary to count the total number (by zip) of how many 911 calls had initial call types of unconsciousness or cardiac arrest cases       
zipInstanceCount = dict()

#for the numerator: create a dictionary to calculate the total # of people that actaully died based on the incidents from the denominator
actDeathCount = dict()

#read the first line of the data
line = data.readline()
#loop through each line of the data
while line:
    #split the tab-delimited line into fields
    fields = re.split('\t', line)
    #if the initial call type (field 3) is either a cardiac arrest or unconsciousness case                     
    if fields[2] == "ARREST" or fields[2] == "UNC":
        #count by zip code how many such records there are altogether 
        #get the zipcode (field 22) and set that as the key
        key = fields[21]
        #if the key is not already in the zipInstanceCount dictionary 
        if key not in zipInstanceCount:
            #set that keys count equal to 1
            zipInstanceCount[key] = 1
        #otherwise 
        else:
            #add 1 to the count
            zipInstanceCount[key] += 1
            
        #count how many actually died (feild $19)
        #if (feild $19) contains the number 83 : code for a call resulting in death
        if fields[18] == "83":
            #if the key is not already in the actDeathCount dictionary
            if key not in actDeathCount:
                #set that keys count equal to 1  
                actDeathCount[key] = 1
            #otherwise
            else:
                #add 1 to the count 
                actDeathCount[key] += 1
    #get the next 'read line' from the data for the while loop            
    line = data.readline()
#when done looping close the file
data.close()

#create the deathRatio dictionary that takes (by zip) the total # of actual deaths divided by the total # of EMS calls for cardiac arrests or unconsciousness  
deathRatio = dict()
#for every zipcode(key) in the zipInstanceCount dictionary
for key in zipInstanceCount:
    #if that zipcode is also in the actDeathCount
    if key in actDeathCount:
        #divide the numerator and denomenator to get the deathratio by zipcode(key)
        deathRatio[key] = actDeathCount[key]/zipInstanceCount[key]
    #otherwise
    else:
        #set the key's deathratio to 0
        deathRatio[key] = 0

#for every key in the deathRatio dictionary
for key in deathRatio:
    #print to standard out the key followed by a pipe followed by string of deathratio
    print(key +  "|" + str(deathRatio[key]))
        
