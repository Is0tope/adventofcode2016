import math
import operator

from sympy.geometry import Line, Point, intersection, Segment

def deg2vec(angle,mag):
    #0 is [1,0]
    r = math.radians(angle)
    return [mag*round(math.sin(r)),round(mag*math.cos(r))]

lrmap = {'L' : -90, 'R' : 90}

with open("directions.txt") as f:
    dirs = f.readline().replace(" ","").split(",")
    dirs = [(d[0],int(d[1:])) for d in dirs]

    #north (deg)
    angle = 0
    coords = [0,0]
    places = []

    for d in dirs:
        angle += lrmap[d[0]]
        vector = deg2vec(angle,d[1])
        new_coords = map(operator.add,coords,vector)
        ln = Segment(Point(coords[0],coords[1]),Point(new_coords[0],new_coords[1]))
        coords = new_coords
        print coords
        for p in places[:-1]:
            intersect = intersection(p,ln)
            if intersect:
                print "FOUND IT"
                print intersect
                exit(0)
        places.append(ln)