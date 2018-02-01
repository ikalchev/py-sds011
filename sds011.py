"""
"""
import time
#from sensors.SDS011 import SDS011 as AirSensor
from pyhap.accessories._sds011 import SDS011 as AirSensor
from pyhap.accessory import Accessory, Category
import pyhap.loader as loader


class SDS011(Accessory):

    category = Category.SENSOR

    def __init__(self, serial_port, *args, **kwargs):
        self.pm25_density = None
        self.pm10_density = None
        super(SDS011, self).__init__(*args, **kwargs)
        self.serial_port = serial_port
        self.sensor = AirSensor(serial_port)

    def _set_services(self):
        super(SDS011, self)._set_services()
        char_loader = loader.get_char_loader()

        air_quality_pm25 = loader.get_serv_loader().get("AirQualitySensor")
        pm25_size = char_loader.get("AirParticulateSize")
        pm25_size.set_value(0, should_notify=False)
        self.pm25_density = char_loader.get("AirParticulateDensity")
        pm25_name = char_loader.get("Name")
        pm25_name.set_value("PM2.5", should_notify=False)
        air_quality_pm25.get_characteristic("AirQuality")\
                        .set_value(1, should_notify=False)
        air_quality_pm25.add_opt_characteristic(pm25_name, pm25_size, self.pm25_density)

        air_quality_pm10 = loader.get_serv_loader().get("AirQualitySensor")
        pm10_size = char_loader.get("AirParticulateSize")
        pm10_size.set_value(1, should_notify=False)
        self.pm10_density = char_loader.get("AirParticulateDensity")
        pm10_name = char_loader.get("Name")
        pm10_name.set_value("PM10", should_notify=False)
        air_quality_pm10.get_characteristic("AirQuality")\
                        .set_value(1, should_notify=False)
        air_quality_pm10.add_opt_characteristic(pm10_name, pm10_size, self.pm10_density)

        self.add_service(air_quality_pm25)
        self.add_service(air_quality_pm10)

    def __getstate__(self):
        state = super(SDS011, self).__getstate__()
        state["sensor"] = None
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.sensor = AirSensor(self.serial_port)

    def run(self):
        #TODO: read sleep status and if necessary, wake up and set dummy values
        # until it spins properly
        pm25, pm10 = self.sensor.query()
        self.pm25_density.set_value(pm25)
        self.pm10_density.set_value(pm10)
        self.sensor.sleep()
        while not self.run_sentinel.wait(30 * 60):
            self.sensor.sleep(sleep=False)
            time.sleep(15)
            pm25, pm10 = self.sensor.query()
            self.pm25_density.set_value(pm25)
            self.pm10_density.set_value(pm10)
            self.sensor.sleep()
