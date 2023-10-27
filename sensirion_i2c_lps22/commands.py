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
"""
The transfer classes specify the data that is transferred between host and sensor. The generated transfer classes
are used by the driver class and not intended for direct use.
"""

from enum import Enum
from sensirion_driver_adapters.transfer import Transfer
from sensirion_driver_adapters.rx_tx_data import TxData, RxData
from sensirion_driver_support_types.bitfield import BitField, BitfieldContainer


class Whoami(Transfer):
    """Get the chip id."""

    CMD_ID = 0xf

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>B')


class Status(Transfer):
    """Get the status bit. See datasheet for description of the bits."""

    CMD_ID = 0x27

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B')
    rx = RxData('>B')


class GetCtrlReg1(Transfer):
    """
    Get the control register 1.
    See datasheet for description of the options.
    """

    CMD_ID = 0x10

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B')
    rx = RxData('>B')


class SetCtrlReg1(Transfer):
    """
    Set the control register 1.
    See datasheet for description of the options.
    """

    CMD_ID = 0x10

    def __init__(self, register_value):
        self._register_value = register_value

    def pack(self):
        return self.tx_data.pack([self._register_value])

    tx = TxData(CMD_ID, '>BB')


class GetCtrlReg2(Transfer):
    """
    Get the control register 3.
    See datasheet for description of the options.
    """

    CMD_ID = 0x11

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B')
    rx = RxData('>B')


class SetCtrlReg2(Transfer):
    """
    Set the control register 2.
    See datasheet for description of the options.
    """

    CMD_ID = 0x11

    def __init__(self, register_value):
        self._register_value = register_value

    def pack(self):
        return self.tx_data.pack([self._register_value])

    tx = TxData(CMD_ID, '>BB')


class GetCtrlReg3(Transfer):
    """
    Get the control register 3.
    See datasheet for description of the options.
    """

    CMD_ID = 0x12

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B')
    rx = RxData('>B')


class SetCtrlReg3(Transfer):
    """
    Set the control register 3.
    See datasheet for description of the options.
    """

    CMD_ID = 0x12

    def __init__(self, register_value):
        self._register_value = register_value

    def pack(self):
        return self.tx_data.pack([self._register_value])

    tx = TxData(CMD_ID, '>BB')


class ReadPressureOutXl(Transfer):
    """Read current pressure from register, LSB"""

    CMD_ID = 0x28

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>B')


class ReadPressureOutL(Transfer):
    """Read current pressure from register, middle byte"""

    CMD_ID = 0x29

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>B')


class ReadPressureOutH(Transfer):
    """Read current pressure from register, MSB"""

    CMD_ID = 0x2a

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>B')


class ReadPressure(Transfer):
    """Read current pressure in register auto increment mode. The value returned is a two's complement and has a scale factor of 4096 to convert to hPa."""

    CMD_ID = 0x28

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>3B')


class ReadTemperatureL(Transfer):
    """Read temperature measurement from register, LOW byte"""

    CMD_ID = 0x2b

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>B')


class ReadTemperatureH(Transfer):
    """Read temperature measurement from register, high byte"""

    CMD_ID = 0x2c

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>B')


class ReadTemperature(Transfer):
    """
    Read current temperature from registers in auto increment mode.
    The value returned has a scale factor of 100 to convert to degC.
    """

    CMD_ID = 0x2b

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.05, slave_address=None, ignore_ack=False)
    rx = RxData('>2B')


class ResetLowPass(Transfer):
    """
    Low-pass filter reset. If the LPFP is active, in order to avoid the transitory phase, the
    filter can be reset by reading this register before generating pressure measurements.
    """

    CMD_ID = 0x33

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B')


class CtrlRegOneT(BitfieldContainer):
    ODR = BitField(offset=4, width=3)
    EN_LPFP = BitField(offset=3, width=1)
    LPFP_CFG = BitField(offset=2, width=1)
    BDU = BitField(offset=1, width=1)


class CtrlRegTwoT(BitfieldContainer):
    BOOT = BitField(offset=7, width=1)
    FIFO_EN = BitField(offset=6, width=1)
    STOP_ON_FTH = BitField(offset=5, width=1)
    IF_ADD_INC = BitField(offset=4, width=1)
    SWRESET = BitField(offset=2, width=1)
    ONE_SHOT = BitField(offset=0, width=1)


class CtrlRegThreeT(BitfieldContainer):
    INT_H_L = BitField(offset=7, width=1)
    PP_OD = BitField(offset=6, width=1)
    F_FSS5 = BitField(offset=5, width=1)
    F_FTH = BitField(offset=4, width=1)
    F_OVR = BitField(offset=3, width=1)
    DRDY = BitField(offset=2, width=1)
    INT_S2 = BitField(offset=1, width=2)


class StatusT(BitfieldContainer):
    T_OR = BitField(offset=5, width=1)
    P_OR = BitField(offset=4, width=1)
    T_DA = BitField(offset=1, width=1)
    P_DA = BitField(offset=0, width=1)


class OdrFrequency(Enum):
    FREQUENCY1HZ = 1
    FREQUENCY10HZ = 2
    FREQUENCY25HZ = 3
    FREQUENCY50HZ = 4
    FREQUENCY75HZ = 5

    def __int__(self):
        return self.value
