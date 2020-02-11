##############################################
## To use the acceleration measured to   #####
## find the distance for the VN sensor   #####
#############################################
from vnpy import EzAsyncData
#from influxdb import InfluxDBClient
import datetime
import v2.py

from time import sleep

# Connect to Database
#client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
#client.create_database('example')

# Connect to VectorNav
ez = EzAsyncData.connect('/dev/ttyUSB0', 115200)


# Run until the script is terminated
while True:
    json_points = []
    before = datetime.datetime.now()

    #while (datetime.datetime.now() - before).total_seconds() < 1:
        # Get the next batch of data
    cd = ez.next_data()
    time = datetime.datetime.utcnow()

####to call acceleration from v2
    if cd.has_acceleration:
            json_points.append({
                "measurement": "acceleration",
                "time": time,
                "fields": {
                    "x": cd.acceleration.x,
                    "y": cd.acceleration.y,
                    "z": cd.acceleration.z
                }
            })
    print("x= {} ,y= {}, z= {}".format(json_points[fields][x],json_points[fields][y],json_points[fields][x]))
    time.sleep(.001)






###ways to find distance:


