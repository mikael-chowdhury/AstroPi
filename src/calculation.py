import math
from constants import GRAVITATIONAL_CONSTANT, MASS_OF_EARTH, RADIUS_OF_EARTH

def full(data):
    velocity_table = []
    for height in data[4]:
    
        velocity_table.append(math.sqrt(GRAVITATIONAL_CONSTANT*MASS_OF_EARTH/((height + RADIUS_OF_EARTH))))
    return velocity_table

def acceleration(x,y,z):
    acceleration_scalar = []
    for x1,y1,z1 in zip(x,y,z):
        acceleration_scalar.append(math.sqrt(x1**2+y1**2+z1**2))
    return acceleration_scalar

def haverSineCoordinates(lat1,long1,lat2,long2,alt1,alt2,radius): #find distance between two coordinate systems

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    long1 = math.radians(long1)
    long2 = math.radians(long2)

    # Differences in coordinates
    dlat = lat2 - lat1
    dlong = long2 - long1

    # Haversine formula for horizontal distance
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlong / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    xy_distance = radius * c  # Surface distance in meters

    # Altitude difference
    dalt = alt2 - alt1

    # Total distance including altitude
    xyz_distance = math.sqrt(xy_distance**2 + dalt**2)

    return xyz_distance
