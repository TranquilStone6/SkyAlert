from shapely.geometry import Point, LineString, Polygon
import numpy as np
import matplotlib as mpl
import pandas as pd
import geopandas as gpd
point1=Point(1,1)
point2=Point(2,2)
point3=Point(3,3)
Line=LineString([point1,point2,point3])
point4=Point(1,0)
point5=Point(0,1)
point6=Point(0,0)
polygon=Polygon([point1,point4,point6,point5])

fp="Data\DAMSELFISH_distributions.shp"
data=gpd.read_file(fp)
print(data.head())
data.plot()