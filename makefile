#Make PDF of the Graph
all:	graph.pdf

#Remove all created files besides for graph.pdf
clean:
	rm xAxis yAxis zip

#Create the graph's PDF using graph.py and utilize info from zip file
graph.pdf:	zip graph.py
	python3 graph.py

#Create the zip file using zip.py and utilize info from xAxis and yAxis files
zip:		xAxis yAxis zip.py
	python3 zip.py > zip

#Create the yAxis file using y.py and utilize second data source symbolic link
yAxis:		data2  y.py 
	python3 y.py >  yAxis 

#Create the xAxis file using x.py and utilize first data source symbolic link    
xAxis:		data1  x.py  
	python3 x.py > xAxis
