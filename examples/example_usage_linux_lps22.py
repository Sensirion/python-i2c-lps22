#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2023 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:     sensirion-driver-generator 0.33.0
# Product:       lps22
# Model-Version: 1.0.0
#

import argparse
import time
from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection, CrcCalculator
from sensirion_driver_adapters.i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_lps22.device import Lps22Device
from sensirion_i2c_lps22.commands import (OdrFrequency)


parser = argparse.ArgumentParser()
parser.add_argument('--i2c-port', '-p', default='/dev/i2c-1')
args = parser.parse_args()

with LinuxI2cTransceiver(args.i2c_port) as i2c_transceiver:
    channel = I2cChannel(I2cConnection(i2c_transceiver),
                         slave_address=0x5C,
                         crc=CrcCalculator(8, 0x31, 0xff, 0x0))
    sensor = Lps22Device(channel)
    sensor.swreset()
    sensor.start_one_shot_measurement()
    a_status = sensor.status()
    print(f"a_status: {a_status}; "
          )
    a_pressure = sensor.read_pressure()
    print(f"a_pressure: {a_pressure}; "
          )
    a_temperature = sensor.read_temperature()
    print(f"a_temperature: {a_temperature}; "
          )
    sensor.start_continious_measurement(OdrFrequency.FREQUENCY1HZ)
    for i in range(5):
        try:
            time.sleep(1.0)
            a_status = sensor.status()
            print(f"a_status: {a_status}; "
                  )
            a_pressure = sensor.read_pressure_single_bytes()
            print(f"a_pressure: {a_pressure}; "
                  )
            a_temperature = sensor.read_temperature_single_bytes()
            print(f"a_temperature: {a_temperature}; "
                  )
        except BaseException:
            continue
    sensor.stop_continious_measurement()