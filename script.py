## script for initializing the sensor
# Tom's code


from vnpy import EzAsyncData
#from influxdb import InfluxDBClient
import datetime
from time import sleep
# Connect to Database
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
client.create_database('example')
# Connect to VectorNav
ez = EzAsyncData.connect('/dev/ttyUSB0', 115200)
# Run until the script is terminated
while True:
    json_points = []
    before = datetime.datetime.now()
    while (datetime.datetime.now() - before).total_seconds() < 1:
        # Get the next batch of data
        cd = ez.next_data()
        time = datetime.datetime.utcnow
        if cd.has_angular_rate:
            json_points.append({
                "measurement": "angular_rate",
                "time": time,
                "fields": {
                    "x": cd.angular_rate.x,
                    "y": cd.angular_rate.y,
                    "z": cd.angular_rate.z
                }
            })
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
        if cd.has_magnetic:
            json_points.append({
                "measurement": "magnetic",
                "time": time,
                "fields": {
                    "x": cd.magnetic.x,
                    "y": cd.magnetic.y,
                    "z": cd.magnetic.z
                }
            })
        if cd.has_yaw_pitch_roll:
            json_points.append({
                "measurement": "yaw_pitch_roll",
                "time": time,
                "fields": {
                    "x": cd.yaw_pitch_roll.x,
                    "y": cd.yaw_pitch_roll.y,
                    "z": cd.yaw_pitch_roll.z
                }
            })
    # Submit the data to the database every second
    client.write_points(json_points)