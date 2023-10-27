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

import pytest
from sensirion_driver_adapters.i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_driver import I2cConnection
from sensirion_shdlc_driver import ShdlcConnection, ShdlcSerialPort
from sensirion_shdlc_sensorbridge import SensorBridgeShdlcDevice, SensorBridgePort, SensorBridgeI2cProxy

from sensirion_i2c_lps22.device import Lps22Device

from sensirion_i2c_lps22.commands import (OdrFrequency)


@pytest.fixture
def sensor(channel_provider):
    with ShdlcSerialPort(port="COM1", baudrate=460800) as port:
        bridge = SensorBridgeShdlcDevice(ShdlcConnection(port), slave_address=0)
        bridge.set_i2c_frequency(SensorBridgePort.ONE, frequency=400e3)
        bridge.set_supply_voltage(SensorBridgePort.ONE, voltage=3.3)
        bridge.switch_supply_on(SensorBridgePort.ONE)
        i2c_transceiver = SensorBridgeI2cProxy(bridge, port=SensorBridgePort.ONE)
        channel = I2cChannel(I2cConnection(i2c_transceiver), slave_address=0x5C)
        yield Lps22Device(channel)


def test_whoami1(sensor):
    chip_id = sensor.whoami()
    print(f"chip_id: {chip_id}; "
          )


def test_swreset1(sensor):
    sensor.swreset()


def test_power_down_mode1(sensor):
    sensor.power_down_mode()


def test_start_one_shot_measurement1(sensor):
    sensor.start_one_shot_measurement()


def test_status1(sensor):
    a_status = sensor.status()
    print(f"a_status: {a_status}; "
          )


def test_read_pressure1(sensor):
    a_pressure = sensor.read_pressure()
    print(f"a_pressure: {a_pressure}; "
          )


def test_read_temperature1(sensor):
    a_temperature = sensor.read_temperature()
    print(f"a_temperature: {a_temperature}; "
          )


def test_start_continious_measurement1(sensor):
    sensor.start_continious_measurement(OdrFrequency.FREQUENCY1HZ)
    a_status = sensor.status()
    print(f"a_status: {a_status}; "
          )
    a_pressure = sensor.read_pressure_single_bytes()
    print(f"a_pressure: {a_pressure}; "
          )
    a_temperature = sensor.read_temperature_single_bytes()
    print(f"a_temperature: {a_temperature}; "
          )
    sensor.stop_continious_measurement()

