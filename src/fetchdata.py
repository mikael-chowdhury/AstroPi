import pandas as pd 
import ast 
import calculation
from constants import RADIUS_OF_EARTH

def fetchData():
    df = pd.read_csv('../data/results.csv')
    Altitudes = []
    Time = []
    x = []
    y = []
    z = []
    coordinates_array = []
    counter = 0
    for time, acceleration_vector, heights,coordinates in zip(df['time'],df['accelerometer_raw'],df['iss_height'],df['iss_coordinates']):
        
        acceleration_vector = ast.literal_eval(acceleration_vector)

        x.append(float(acceleration_vector['x']))
        y.append(float(acceleration_vector['y']))
        z.append(float(acceleration_vector['z']))

        Altitudes.append(heights)
        if counter == 0:
            subtractor = float(time)
        Time.append(float(time)-subtractor)
        counter+=1

        coordinates = [float(x) for x in coordinates.split(",")]
        coordinates_array.append(coordinates)
    
    return (Time,x,y,z,Altitudes,coordinates_array)

def fetchProcessed():
    data = fetchData()
    velocities = calculation.full(data)
    accelerations = calculation.acceleration(data[1],data[2],data[3])
    return(velocities,data[0],accelerations,data[4])


def fetchDistance():
    data = fetchData()
    length= len(data[5])
    velocity_array = []
    time = []
    distance_array = []
    for i,coordinate in enumerate(data[5]):
        if i != length-1:
            distance = calculation.haverSineCoordinates(data[5][i][0],data[5][i][1],data[5][i+1][0],data[5][i+1][1],data[4][i],data[4][i+1],RADIUS_OF_EARTH+(data[4][i]+data[4][i+1])/2)
            current_time = data[0][i+1]-data[0][0]
            time.append(current_time)
            distance_array.append(distance)
            try: 
                velocity_array.append(distance/(current_time-time[i-1]))
            except:
                velocity_array.append(distance)

    returnframe = pd.DataFrame()
    returnframe['Velocity'] = velocity_array
    returnframe['Time'] = time
    returnframe['Distance'] = distance_array

    returnframe.to_csv('./velocities.csv')
    return(velocity_array,time)

    


