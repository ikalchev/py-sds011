# py-sds011

This is a python 3 interface to the SDS011 air particulate density sensor. The
datasheet, which this implementation follows, can be found [here](https://cdn.sparkfun.com/assets/parts/1/2/2/7/5/Laser_Dust_Sensor_Control_Protocol_V1.3.pdf).

Depends on `pyserial`.
# API
```python
>>> sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
>>> sensor.query()  # Gets (pm25, pm10)
(15.6, 20.3)
>>> sensor.sleep()  # Turn off fan and diode
>>> sensor.sleep(sleep=False)  # Turn on fan and diode
>>> time.sleep(15)  # Allow time for the sensor to measure properly
>>> sensor.query()
(16.2, 21.0)
>>> # There are other methods to configure the device, go check them out.
```

