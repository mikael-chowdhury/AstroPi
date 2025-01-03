from sense_hat import SenseHat
import time
from skyfield.api import load
from astro_pi_orbit import ISS

class GlobalSense:
    def __init__(self):
        self.sense = SenseHat()
        self.sense.color.gain = 60
        self.sense.color.integration_cycles = 64

        # self.result_labels = ["accelerometer", "accelerometer_raw", "gyroscope", "gyroscope_raw", "compass", "magnetic field", "humidity", "orientation", "orientation_degrees", "pressure", "temperature", "time", "time_to_fetch", "iss_height", "iss_coordinates"]
        self.result_labels = ["accelerometer_raw", "time", "iss_height", "iss_coordinates"]
        self.results = [[] for _ in self.result_labels]

        self.iss = ISS()

    def get_results(self):
        return self.results

    def get_accelerometer(self):
        result = self.sense.get_accelerometer()
        self.results[0].append(result)
        return result
    
    def get_accelerometer_raw(self):
        result = self.sense.get_accelerometer_raw()
        # self.results[1].append(result)
        self.results[0].append(result)
        return result
    
    def get_gyroscope(self):
        result = self.sense.get_gyroscope()
        self.results[2].append(result)
        return result

    def get_gyroscope_raw(self):
        result = self.sense.get_gyroscope_raw()
        self.results[3].append(result)
        return result

    def get_compass(self):
        result = self.sense.get_compass()
        self.results[4].append(result)
        return result

    def get_magnetometer_data(self):
        result = self.sense.get_compass_raw()
        self.results[5].append(result)
        return result
    
    def get_humidity(self):
        result = self.sense.get_humidity()
        self.results[6].append(result)
        return result

    def get_orientation(self):
        result = self.sense.get_orientation()
        self.results[7].append(result)
        return result
    
    def get_orientation_degrees(self):
        result = self.sense.get_orientation_degrees()
        self.results[8].append(result)
        return result

    def get_pressure(self):
        result = self.sense.get_pressure()
        self.results[9].append(result)
        return result
    
    def get_temperature(self):
        result = self.sense.get_temperature()
        self.results[10].append(result)
        return result

    def get_iss_height(self):
        stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
        satellites = load.tle_file(stations_url)
        by_name = {sat.name: sat for sat in satellites}
        satellite = by_name['ISS (ZARYA)']
        
        ts = load.timescale()
        t = ts.now()
        geocentric = satellite.at(t)

        subpoint = geocentric.subpoint()
        height_km = subpoint.elevation.m
        # self.results[13].append(height_km)
        self.results[2].append(height_km)
        return height_km
    
    def get_iss_coordinates(self):
        point = self.iss.coordinates()
        res = f"{point.latitude.degrees}, {point.longitude.degrees}"
        # self.results[14].append(res)
        self.results[3].append(res)
        return res

    def run_tests(self):
        ######## ACCELEROMETER DATA ########
        # self.get_accelerometer()
        self.get_accelerometer_raw()

        ######### GYROSCOPE DATA ##########
        # self.get_gyroscope()
        # self.get_gyroscope_raw()

        ########## COMPASS DATA ###########
        # self.get_compass()
        # self.get_magnetometer_data()

        ######## ORIENTATION DATA #########
        # self.get_orientation()
        # self.get_orientation_degrees()

        ########### OTHER DATA ############
        # self.get_pressure()
        # self.get_humidity()
        # self.get_temperature()

        ########### ISS COORDS ############
        self.get_iss_height()
        self.get_iss_coordinates()

        self.results[1].append(time.time())