# Linux-Data-Parsing-Project
My hypothesis is: The likelihood of death after a 911 call in a (NY) poor neighborhood is more than in a (NY) rich neighborhood (2006-2010).

My large data source:
https://data.cityofnewyork.us/Public-Safety/EMS-Incident-Dispatch-Data/76xm-jjuj
my symbolic link data1 links to: /data/raw/NYC_EMS_Incidents

my secondary data source is:
http://www.psc.isr.umich.edu/dis/census/Features/tract2zip/index.html (Links to an external site.)
my symbolic link data1 links to: /data/raw/Incomepop.gz

To accomplish my goal, I needed to get a death ratio as my x coordinate and a median income as my y coordinate and have these variables be dependent on their zipcodes.
My makeFile consists of 4 files I created to acomplish my final graph of my hypotheses.

xAxis = To get the death ratio:
For the numerator, I had to retrieve an initial call type (field 3) of either cardiac arrest or unconsciousness and count by zip code (field 20), how many such records were there altogether.
For the denominator, I had to calculate how many people actually died after these incidents. The result of the incident can be found in field19. The code '83' refers to someone who died due to the incident. Dividing the denominator by the numerator gives you the resulting death ratio based on zip code. Then, I printed the zip code followed by a pipe followed by the death ratio. The makefile prints this data to the file called xAxis.

yAxis = To get the median income: I had to retrieve the median income (field 2) based on zip codes(field 1) in NY. The result prints the zip code followed by a pipe followed by the median income. The makefile prints this data to the file called yAxis.

zip = To combine the zipcodes and get the ordered pairs based on each zip: I created three dictionaries. The first dictionary had the zip code as the key and the x coordinate as the data. The second dictionary had the zip code as the key and the y coordinate as the data. The third dictionary combined the two dictionaries by checking if the death ratio zip codes were in median income zip codes. If they were, this new dictionary creates an ordered pair (or a list) of the x and y coordinates as the data and their zip code as the key. As a result, I print the zipcode followed by a pipe, followed by the x coordinate, followed by another pipe followed by the y coordinate. The make file prints this datato the file called zip.

graph.pdf = To get the final graph: I created two dictionaries to put the x and y coordinates in. I used matplotlib to create a scatterplot figure of these points that later creates a pdf called graph.pdf. 

Each dot on my chart is a zip code based on the death ratio and median income. My hypothesis is correct as in most cases, the numerator of the fraction gets larger the poorer you are, and the numerator is smaller the richer you are.    
