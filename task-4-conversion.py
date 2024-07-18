'''here we convert the distance object calculated to other units'''


nairobi =[-1.2858226521480587, 36.81829733363576]
thika=[-1.034827265685195, 37.0766643277757]
mwingi=[-0.9374186346062278, 38.06049881749188]

#initialize the calculator
dist=QgsDistanceArea()

#set the elliposoid to compute with
dist.setEllipsoid('WGS84')

#make the coords qgsPoint objects
point1=QgsPointXY(nairobi[0], nairobi[1])
point2=QgsPointXY(thika[0],thika[1])
point3=QgsPointXY(mwingi[0],mwingi[1])

distance1=dist.measureLine(point1,point2)
distance2=dist.measureLine(point2,point3)
total=distance1+distance2
print("Distance from Nairobi to Mwingi via Thika")
print(f'Distance in Kms: {total/1000}')

#convert from km to miles
'''
the convertLengthMeasurement method of dist(QgsDistanceArea) class 
takes 2 arguments. 
1. the distance object to convert
2. the units of distance of the Qgis.DistanceUnit class

'''
distance_miles=dist.convertLengthMeasurement(total, Qgis.DistanceUnit.DistanceMiles)
print(f'Distance in miles : {distance_miles}')

distance_degrees=dist.convertLengthMeasurement(total, Qgis.DistanceUnit.DistanceDegrees)
print(f'Distance in degrees : {distance_degrees}')

distance_feet=dist.convertLengthMeasurement(total, Qgis.DistanceUnit.DistanceFeet)
print(f'Distance in imperial feet : {distance_feet}')

distance_yards=dist.convertLengthMeasurement(total, Qgis.DistanceUnit.DistanceYards)
print(f'Distance in imperial yards : {distance_yards}')
