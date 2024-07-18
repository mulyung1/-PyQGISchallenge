nairobi =[-1.2858226521480587, 36.81829733363576]
thika=[-1.034827265685195, 37.0766643277757]
mwingi=[-0.9374186346062278, 38.06049881749188]


#initialize the 
dist=QgsDistanceArea()

#set the elliposoid to compute with
dist.setEllipsoid('WGS84')

#make the coords qgsPoint objects
point1=QgsPointXY(nairobi[0], nairobi[1])
point2=QgsPointXY(thika[0],thika[1])
point3=QgsPointXY(mwingi[0],mwingi[1])

distance1=dist.measureLine(point1,point2)
distance2=dist.measureLine(point2,point3)

print((distance1+distance2)/1000)
