#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2023 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:     sensirion-driver-generator 0.33.0
# Product:       lps22
# Model-Version: 1.0.1
#

import argparse
import time
from sensirion_i2c_driver import I2cConnection, CrcCalculator
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sensorbridge import (SensorBridgePort,
                                          SensorBridgeShdlcDevice,
                                          SensorBridgeI2cProxy)
from sensirion_driver_adapters.i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_lps22.device import Lps22Device
from sensirion_i2c_lps22.commands import (OdrFrequency)


parser = argparse.ArgumentParser()
parser.add_argument('--serial-port', '-p', default='COM1')
args = parser.parse_args()

with ShdlcSerialPort(port=args.serial_port, baudrate=460800) as port:
    bridge = SensorBridgeShdlcDevice(ShdlcConnection(port), slave_address=0)
    bridge.set_i2c_frequency(SensorBridgePort.ONE, frequency=400e3)
    bridge.set_supply_voltage(SensorBridgePort.ONE, voltage=3.3)
    bridge.switch_supply_on(SensorBridgePort.ONE)
    i2c_transceiver = SensorBridgeI2cProxy(bridge, port=SensorBridgePort.ONE)
    channel = I2cChannel(I2cConnection(i2c_transceiver),
                         slave_address=0x5C)
    sensor = Lps22Device(channel)
    sensor.swreset()
    sensor.start_one_shot_measurement()
    data_ready = False
    while not data_ready:
        time.sleep(0.1)
        a_status = sensor.status()
        data_ready = a_status.P_DA and a_status.T_DA
    a_pressure = sensor.read_pressure()
    print(f"a_pressure: {a_pressure}; "
          )
    a_temperature = sensor.read_temperature()
    print(f"a_temperature: {a_temperature}; "
          )

    sensor.start_continious_measurement(OdrFrequency.FREQUENCY1HZ)
    for i in range(20):
        try:
            data_ready = False
            while not data_ready:
                time.sleep(0.1)
                a_status = sensor.status()
                data_ready = a_status.P_DA and a_status.T_DA
            a_pressure = sensor.read_pressure_single_bytes()
            print(f"a_pressure: {a_pressure}; "
                  )
            a_temperature = sensor.read_temperature_single_bytes()
            print(f"a_temperature: {a_temperature}; "
                  )
        except BaseException:
            continue
    sensor.stop_continious_measurement()
