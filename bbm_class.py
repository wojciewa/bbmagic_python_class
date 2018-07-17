######################################################################################
# Descirption: BBMagic class use the bbmagic_lib for support the BBMagic devices.
#              Site of BBMagic project is http://bbmagic.net
# author: Gabriel Zima (z1mEk)
# e-mail: gabriel.zima@wp.pl
# github: https://github.com/z1mEk/bbmagic_python_class.git
# create date: 2018-07-02
# update date: 2018-07-09
# compatibile bbmagic_lib version: 1.4
######################################################################################

import json
import ctypes
from ctypes import *
bbm_bt_lib = ctypes.CDLL("bbmagic_lib_1.4.so")

class BBMagic:
    def __init__(self):

        # BBMagic device types
        #-----------------------------------------------------------------------------    
        self.BBMAGIC_M_METEO                      = 1
        self.BBMAGIC_M_MOTION                     = 2
        self.BBMAGIC_M_BUTTON                     = 3
        self.BBMAGIC_M_FLOOD                      = 4
        self.BBMAGIC_M_MAGNETO                    = 5
        self.BBMAGIC_M_LINUXDEVICE                = 6
        self.BBMAGIC_M_RELAY                      = 20
        self.BBMAGIC_M_DIMMER                     = 21
        self.BBMAGIC_M_KYE_REG                    = 0xFE
        self.BBMAGIC_M_UNKNOWN                    = 0xFF

        # BBMagic Lib buffer offsets for all devices
        #------------------------------------------------------------------------------
        # BBMagic device ID
        self.BBMAGIC_DEVICE_TYPE                  = 4
        # Bluetooth device address
        self.BBMAGIC_DEVICE_ADDR_5                = 16
        self.BBMAGIC_DEVICE_ADDR_4                = 17
        self.BBMAGIC_DEVICE_ADDR_3                = 18
        self.BBMAGIC_DEVICE_ADDR_2                = 19
        self.BBMAGIC_DEVICE_ADDR_1                = 20
        self.BBMAGIC_DEVICE_ADDR_0                = 21
        # Bluetooth Radio Signal Strength Indicator
        self.BBMAGIC_DEVICE_RSSI                  = 22
        # Divider to calculate module supply voltage in Volts
        self.BBMAGIC_VCC_DIVIDER                  = 71.0

        # BBMagic Lib buffer offsets
        #------------------------------------------------------------------------------
        # BBMagic METEO module
        self.BBM_METEO_WORKTIME_0                 = 0
        self.BBM_METEO_WORKTIME_1                 = 1
        self.BBM_METEO_WORKTIME_2                 = 2
        self.BBM_METEO_WORKTIME_3                 = 3
        self.BBM_METEO_V_SUP                      = 5
        self.BBM_METEO_ADV_TIME                   = 6
        self.BBM_METEO_DIN_STATE                  = 7
        self.BBM_METEO_TEMPER_MSB                 = 8
        self.BBM_METEO_TEMPER_LSB                 = 9
        self.BBM_METEO_HUM                        = 10
        self.BBM_METEO_LIGHT                      = 11
        self.BBM_METEO_ADC_1_MSB                  = 12
        self.BBM_METEO_ADC_1_LSB                  = 13
        self.BBM_METEO_ADC_2_MSB                  = 14
        self.BBM_METEO_ADC_2_LSB                  = 15

        # BBMagic BUTTON module
        self.BBM_BUTTON_SIGN_0                    = 0
        self.BBM_BUTTON_SIGN_1                    = 1
        self.BBM_BUTTON_SIGN_2                    = 2
        self.BBM_BUTTON_SIGN_3                    = 3
        self.BBM_BUTTON_V_SUP                     = 5
        self.BBM_BUTTON_BUTTON_FUNCTION           = 7
        self.BBM_BUTTON_INPUT_PINS                = 8
        self.BBM_BUTTON_CHIP_TEMP                 = 9
        self.BBM_BUTTON_LIGHT                     = 10
        self.BBM_BUTTON_FIRM_1                    = 14
        self.BBM_BUTTON_FIRM_0                    = 15
        self.BBM_BUTTON_FN_SINGLE_CLICK           = 1
        self.BBM_BUTTON_FN_DOUBLE_CLICK           = 2
        self.BBM_BUTTON_FN_HOLDING                = 3

        # BBMagic MOTION module
        self.BBM_MOTION_WORKTIME_0                = 0
        self.BBM_MOTION_WORKTIME_1                = 1
        self.BBM_MOTION_WORKTIME_2                = 2
        self.BBM_MOTION_WORKTIME_3                = 3
        self.BBM_MOTION_V_SUP                     = 5
        self.BBM_MOTION_FLAGS                     = 7
        self.BBM_MOTION_CHIP_TEMP                 = 8
        self.BBM_MOTION_LIGHT                     = 9
        self.BBM_MOTION_ADC_1_MSB                 = 10
        self.BBM_MOTION_ADC_1_LSB                 = 11
        self.BBM_MOTION_ADC_2_MSB                 = 12
        self.BBM_MOTION_ADC_2_LSB                 = 13
        self.BBM_MOTION_FIRM_1                    = 14
        self.BBM_MOTION_FIRM_0                    = 15
        self.BBM_MOTION_ALERT_MASK                = 0x80

        # BBMagic FLOOD module
        self.BBM_FLOOD_WORKTIME_0                 = 0
        self.BBM_FLOOD_WORKTIME_1                 = 1
        self.BBM_FLOOD_WORKTIME_2                 = 2
        self.BBM_FLOOD_WORKTIME_3                 = 3
        self.BBM_FLOOD_V_SUP                      = 5
        self.BBM_FLOOD_ADV_TIME                   = 6
        self.BBM_FLOOD_ALERT_FLAGS                = 7
        self.BBM_FLOOD_CHIP_TEMP                  = 8
        self.BBM_FLOOD_FIRM_1                     = 14
        self.BBM_FLOOD_FIRM_0                     = 15
        self.BBM_FLOOD_ALERT_MASK                 = 0x01

        # BBMagic MAGNETO module
        self.BBM_MAGNETO_WORKTIME_0               = 0
        self.BBM_MAGNETO_WORKTIME_1               = 1
        self.BBM_MAGNETO_WORKTIME_2               = 2
        self.BBM_MAGNETO_WORKTIME_3               = 3
        self.BBM_MAGNETO_V_SUP                    = 5
        self.BBM_MAGNETO_ADV_TIME                 = 6
        self.BBM_MAGNETO_FLAGS                    = 7
        self.BBM_MAGNETO_CHIP_TEMP                = 8
        self.BBM_MAGNETO_LIGHT                    = 9
        self.BBM_MAGNETO_ADC_1_MSB                = 10
        self.BBM_MAGNETO_ADC_1_LSB                = 11
        self.BBM_MAGNETO_ADC_2_MSB                = 12
        self.BBM_MAGNETO_ADC_2_LSB                = 13
        self.BBM_MAGNETO_FIRM_1                   = 14
        self.BBM_MAGNETO_FIRM_0                   = 15
        self.BBM_MAGNETO_MAGNET_MASK              = 0x80
        self.BBM_MAGNETO_IN_0_BIT                 = 0x01
        self.BBM_MAGNETO_IN_1_BIT                 = 0x02
        self.BBM_MAGNETO_IN_2_BIT                 = 0x04
        self.BBM_MAGNETO_IN_3_BIT                 = 0x08

        # LINUX DEVICE with BBM LIB
        self.BBM_LINUXLIB_TIMESTAMP_0             = 0
        self.BBM_LINUXLIB_TIMESTAMP_1             = 1
        self.BBM_LINUXLIB_TIMESTAMP_2             = 2
        self.BBM_LINUXLIB_TIMESTAMP_3             = 3
        self.BBM_LINUXLIB_DEST_ADDR_5             = 5
        self.BBM_LINUXLIB_DEST_ADDR_4             = 6
        self.BBM_LINUXLIB_DEST_ADDR_3             = 7
        self.BBM_LINUXLIB_DEST_ADDR_2             = 8
        self.BBM_LINUXLIB_DEST_ADDR_1             = 9
        self.BBM_LINUXLIB_DEST_ADDR_0             = 10
        self.BBM_LINUXLIB_DATA_0                  = 11
        self.BBM_LINUXLIB_DATA_1                  = 12
        self.BBM_LINUXLIB_DATA_2                  = 13
        self.BBM_LINUXLIB_VER_1                   = 14
        self.BBM_LINUXLIB_VER_0                   = 15

        # BBMagic RELAY module
        self.BBM_RELAY_WORKTIME_0                 = 0
        self.BBM_RELAY_WORKTIME_1                 = 1
        self.BBM_RELAY_WORKTIME_2                 = 2
        self.BBM_RELAY_WORKTIME_3                 = 3
        self.BBM_RELAY_V_SUP                      = 5
        self.BBM_RELAY_ADV_TIME                   = 6
        self.BBM_RELAYS_STATE                     = 7
        self.BBM_RELAY_CHIP_TEMP                  = 8
        self.BBM_RELAY_LIGHT                      = 9
        self.BBM_RELAY_ADC_1_MSB                  = 10
        self.BBM_RELAY_ADC_1_LSB                  = 11
        self.BBM_RELAY_ADC_2_MSB                  = 12
        self.BBM_RELAY_ADC_2_LSB                  = 13
        self.BBM_RELAY_FIRM_1                     = 14
        self.BBM_RELAY_FIRM_0                     = 15
        self.BBM_RELAY_0                          = 1
        self.BBM_RELAY_1                          = 2
        self.BBM_RELAY_2                          = 4
        self.BBM_RELAY_3                          = 8

        # BBMagic DIMMER module
        self.BBM_DIMMER_WORKTIME_0                = 0
        self.BBM_DIMMER_WORKTIME_1                = 1
        self.BBM_DIMMER_WORKTIME_2                = 2
        self.BBM_DIMMER_WORKTIME_3                = 3
        self.BBM_DIMMER_V_SUP                     = 5
        self.BBM_DIMMER_ADV_TIME                  = 6
        self.BBM_DIMMER_CHIP_TEMP                 = 7
        self.BBM_DIMMER_LIGHT                     = 8
        self.BBM_DIMMER_CH0                       = 9
        self.BBM_DIMMER_CH1                       = 10
        self.BBM_DIMMER_CH2                       = 11
        self.BBM_DIMMER_ADC_1_MSB                 = 12
        self.BBM_DIMMER_ADC_1_LSB                 = 13
        self.BBM_DIMMER_FIRM_1                    = 14
        self.BBM_DIMMER_FIRM_0                    = 15

        #------------------------------------------------------------------------------

        self.BBLIB_FRAME_SIZE                     = 23
        self.BBM_BT_ADDR_SIZE                     = 6

        self.bbm_buf = (c_byte * self.BBLIB_FRAME_SIZE)()

    # Function: open bt hci and starts bt scanning
    # Arguments: int led_rx_pin, int led_tx_pin, int led_run_pin, int op_mode
    def bbm_bt_open(self, *args, **kwargs):
        led_rx_pin = kwargs.get('led_rx_pin', 0)
        led_tx_pin = kwargs.get('led_tx_pin', 0)
        led_run_pin = kwargs.get('led_run_pin', 0)
        op_mode = kwargs.get('op_mode', 1)
        return bbm_bt_lib.bbm_bt_open(led_rx_pin, led_tx_pin, led_run_pin, op_mode)

    # Function: stops bt scanning and closes bt hci
    def bbm_bt_close(self):
        return bbm_bt_lib.bbm_bt_close()

    # Function: reads data from bbmagic modules
    def bbm_bt_read(self, bbm_data):
        i = bbm_bt_lib.bbm_bt_read(byref(self.bbm_buf))
        bbm_data = [x for x in self.bbm_buf]
        return i

    # Function: returns version of bbm_bt library
    def bbm_bt_lib_version(self):
        v = bbm_bt_lib.bbm_bt_lib_version()object
        return "{:x}".format(v)

    # Function: turns on bbm relays
    def bbm_bt_relay_on(self, mac, relay):
        i = bbm_bt_lib.bbm_bt_relay_on(self.mac2buf(mac), [1,2,4,8][relay])
        return i

    # Function: turns off selected relays
    def bbm_bt_relay_off(self, mac, relay):
        i = bbm_bt_lib.bbm_bt_relay_off(self.mac2buf(mac), [1,2,4,8][relay])
        return i

    # Function: sets bbm dimmer channels
    def bbm_bt_dimmer(self, mac, red, green, blue):
        rgb = [red, green, blue]
        channel = (c_byte * len(rgb))(*rgb)
        i = bbm_bt_lib.bbm_bt_dimmer(self.mac2buf(mac), channel)
        return i

    ### Helper functions
    # Function mac to buffer
    def buf2mac(self, buf, range_from, range_to):
        buf_bytes = bytearray(buf)
        device_mac = ''
        for i in range(range_from, range_to + 1):
            device_mac += "{:x}".format(buf_bytes[i])
        return device_mac.upper()

    # Function mac to buffer
    def mac2buf(self, mac):
        mac_buf = (c_byte * self.BBM_BT_ADDR_SIZE)()
        mac_buf = [int(mac[x:x+2], 16) for x in range(0, len(mac), 2)]
        return mac_buf

    # Function: read data from bbmagic modules and append to dictionary
    def bbm_read_dict(self):
        i = self.bbm_bt_read(self.bbm_buf)
        self.bbm_buf_bytes = bytearray(self.bbm_buf)
        d = dict()
        d['result'] = i

        if i > 0:
            d['mac'] = self.buf2mac(self.bbm_buf, self.BBMAGIC_DEVICE_ADDR_5, self.BBMAGIC_DEVICE_ADDR_0) 
            d['rssi'] = self.bbm_buf[self.BBMAGIC_DEVICE_RSSI]
            device_type = self.bbm_buf[self.BBMAGIC_DEVICE_TYPE]
            d['type'] = device_type

            if device_type == self.BBMAGIC_M_METEO:
                d['type_name'] = 'bbm_meteo'
                d['work_time'] = self.bbm_buf_bytes[self.BBM_METEO_WORKTIME_3] << 24 | \
                                 self.bbm_buf_bytes[self.BBM_METEO_WORKTIME_2] << 16 | \
                                 self.bbm_buf_bytes[self.BBM_METEO_WORKTIME_1] << 8 | \
                                 self.bbm_buf_bytes[self.BBM_METEO_WORKTIME_0]
                d['v_supl'] = "{:4.2f}".format(float(self.bbm_buf_bytes[self.BBM_METEO_V_SUP]) / self.BBMAGIC_VCC_DIVIDER)
                d['adv_time'] = self.bbm_buf[self.BBM_METEO_ADV_TIME] * 2
                d['light'] = self.bbm_buf[self.BBM_METEO_LIGHT]
                d['din_state'] = self.bbm_buf[self.BBM_METEO_DIN_STATE]
                d['meteo_temp'] = "{:4.2f}".format(float(self.bbm_buf[self.BBM_METEO_TEMPER_MSB] << 8 | \
                                 self.bbm_buf[self.BBM_METEO_TEMPER_LSB]) / 100.0)
                d['meteo_hum'] = self.bbm_buf[self.BBM_METEO_HUM]
                d['adc1'] = "{:4.3f}".format(float(self.bbm_buf[self.BBM_METEO_ADC_1_MSB] << 8 | \
                                 self.bbm_buf[self.BBM_METEO_ADC_1_LSB]) / 1000.0)
                d['adc2'] = "{:4.3f}".format(float(self.bbm_buf[self.BBM_METEO_ADC_2_MSB] << 8 | \
                                 self.bbm_buf[self.BBM_METEO_ADC_2_LSB]) / 1000.0)

            elif device_type == self.BBMAGIC_M_MOTION:
                d['type_name'] = 'bbm_motion'
                d['work_time'] = self.bbm_buf_bytes[self.BBM_MOTION_WORKTIME_3] << 24 | \
                                 self.bbm_buf_bytes[self.BBM_MOTION_WORKTIME_2] << 16 | \
                                 self.bbm_buf_bytes[self.BBM_MOTION_WORKTIME_1] << 8 | \
                                 self.bbm_buf_bytes[self.BBM_MOTION_WORKTIME_0]
                d['v_supl'] = "{:4.2f}".format(float(self.bbm_buf_bytes[self.BBM_MOTION_V_SUP]) / self.BBMAGIC_VCC_DIVIDER)
                d['chip_temp'] = self.bbm_buf[self.BBM_MOTION_CHIP_TEMP]
                d['light'] = self.bbm_buf[self.BBM_MOTION_LIGHT]
                d['firmware'] = "{:x}.{:x}".format(self.bbm_buf[self.BBM_MOTION_FIRM_1], self.bbm_buf[self.BBM_MOTION_FIRM_0])
                d['motion_flags'] = self.bbm_buf[self.BBM_MOTION_FLAGS]
                d['adc1'] = "{:4.3f}".format(float(self.bbm_buf[self.BBM_MOTION_ADC_1_MSB] << 8 | \
                                 self.bbm_buf[self.BBM_MOTION_ADC_1_LSB]) / 1000.0)
                d['adc2'] = "{:4.3f}".format(float(self.bbm_buf[self.BBM_MOTION_ADC_2_MSB] << 8 | \
                                 self.bbm_buf[self.BBM_MOTION_ADC_2_LSB]) / 1000.0)

            elif device_type == self.BBMAGIC_M_BUTTON:
                d['type_name'] = 'bbm_button'
                d['button_sign'] = self.bbm_buf_bytes[self.BBM_BUTTON_SIGN_3] << 24 | \
                                 self.bbm_buf_bytes[self.BBM_BUTTON_SIGN_2] << 16 | \
                                 self.bbm_buf_bytes[self.BBM_BUTTON_SIGN_1] << 8 | \
                                 self.bbm_buf_bytes[self.BBM_BUTTON_SIGN_0]
                d['v_supl'] = "{:4.2f}".format(float(self.bbm_buf_bytes[self.BBM_BUTTON_V_SUP]) / self.BBMAGIC_VCC_DIVIDER)
                d['chip_temp'] = self.bbm_buf[self.BBM_BUTTON_CHIP_TEMP]
                d['light'] = self.bbm_buf[self.BBM_BUTTON_LIGHT]
                d['firmware'] = "{:x}.{:x}".format(self.bbm_buf[self.BBM_BUTTON_FIRM_1], self.bbm_buf[self.BBM_BUTTON_FIRM_0])
                d['button_function'] = self.bbm_buf[self.BBM_BUTTON_BUTTON_FUNCTION]
                d['button_input_pins'] = self.bbm_buf[self.BBM_BUTTON_INPUT_PINS]

            elif device_type == self.BBMAGIC_M_FLOOD:
                d['type_name'] = 'bbm_flood'
                d['work_time'] = self.bbm_buf_bytes[self.BBM_FLOOD_WORKTIME_3] << 24 | \
                                 self.bbm_buf_bytes[self.BBM_FLOOD_WORKTIME_2] << 16 | \
                                 self.bbm_buf_bytes[self.BBM_FLOOD_WORKTIME_1] << 8 | \
                                 self.bbm_buf_bytes[self.BBM_FLOOD_WORKTIME_0]
                d['v_supl'] = "{:4.2f}".format(float(self.bbm_buf_bytes[self.BBM_FLOOD_V_SUP]) / self.BBMAGIC_VCC_DIVIDER)
                d['adv_time'] = self.bbm_buf[self.BBM_FLOOD_ADV_TIME] * 2
                d['chip_temp'] = self.bbm_buf[self.BBM_FLOOD_CHIP_TEMP]
                d['firmware'] = "{:x}.{:x}".format(self.bbm_buf[self.BBM_FLOOD_FIRM_1], self.bbm_buf[self.BBM_FLOOD_FIRM_0])
                d['flood_flags'] = self.bbm_buf[self.BBM_FLOOD_ALERT_FLAGS]

            elif device_type == self.BBMAGIC_M_MAGNETO:
                d['type_name'] = 'bbm_magneto'
                d['work_time'] = self.bbm_buf_bytes[self.BBM_MAGNETO_WORKTIME_3] << 24 | \
                                 self.bbm_buf_bytes[self.BBM_MAGNETO_WORKTIME_2] << 16 | \
                                 self.bbm_buf_bytes[self.BBM_MAGNETO_WORKTIME_1] << 8 | \
                                 self.bbm_buf_bytes[self.BBM_MAGNETO_WORKTIME_0]
                d['v_supl'] = "{:4.2f}".format(float(self.bbm_buf_bytes[self.BBM_MAGNETO_V_SUP]) / self.BBMAGIC_VCC_DIVIDER)
                d['adv_time'] = self.bbm_buf[self.BBM_MAGNETO_ADV_TIME] * 2
                d['chip_temp'] = self.bbm_buf[self.BBM_MAGNETO_CHIP_TEMP]
                d['light'] = self.bbm_buf[self.BBM_MAGNETO_LIGHT]
                d['firmware'] = "{:x}.{:x}".format(self.bbm_buf[self.BBM_MAGNETO_FIRM_1], self.bbm_buf[self.BBM_MAGNETO_FIRM_0])
                d['magneto_flags'] = self.bbm_buf[self.BBM_MAGNETO_FLAGS]
                d['adc1'] = "{:4.3f}".format(float(self.bbm_buf[self.BBM_MAGNETO_ADC_1_MSB] << 8 | \
                                 self.bbm_buf[self.BBM_MAGNETO_ADC_1_LSB]) / 1000.0)
                d['adc2'] = "{:4.3f}".format(float(self.bbm_buf[self.BBM_MAGNETO_ADC_2_MSB] << 8 | \
                                 self.bbm_buf[self.BBM_MAGNETO_ADC_2_LSB]) / 1000.0)

            elif device_type == self.BBMAGIC_M_RELAY:
                d['type_name'] = 'bbm_relay'
                d['work_time'] = self.bbm_buf_bytes[self.BBM_RELAY_WORKTIME_3] << 24 | \
                                 self.bbm_buf_bytes[self.BBM_RELAY_WORKTIME_2] << 16 | \
                                 self.bbm_buf_bytes[self.BBM_RELAY_WORKTIME_1] << 8 | \
                                 self.bbm_buf_bytes[self.BBM_RELAY_WORKTIME_0]
                d['v_supl'] = "{:4.2f}".format(float(self.bbm_buf_bytes[self.BBM_RELAY_V_SUP]) / self.BBMAGIC_VCC_DIVIDER)
                d['adv_time'] = self.bbm_buf[self.BBM_RELAY_ADV_TIME] * 2
                d['chip_temp'] = self.bbm_buf[self.BBM_RELAY_CHIP_TEMP]
                d['light'] = self.bbm_buf[self.BBM_RELAY_LIGHT]
                d['firmware'] = "{:x}.{:x}".format(self.bbm_buf[self.BBM_RELAY_FIRM_1], self.bbm_buf[self.BBM_RELAY_FIRM_0])
                d['relays_state'] = self.bbm_buf[self.BBM_RELAYS_STATE]
                d['relays'] = [int(x) for x in list('{:04b}'.format(self.bbm_buf[self.BBM_RELAYS_STATE]))]
                d['adc1'] = "{:4.3f}".format(float(self.bbm_buf[self.BBM_RELAY_ADC_1_MSB] << 8 | \
                                 self.bbm_buf[self.BBM_RELAY_ADC_1_LSB]) / 1000.0)
                d['adc2'] = "{:4.3f}".format(float(self.bbm_buf[self.BBM_RELAY_ADC_2_MSB] << 8 | \
                                 self.bbm_buf[self.BBM_RELAY_ADC_2_LSB]) / 1000.0)

            elif device_type == self.BBMAGIC_M_DIMMER:
                d['type_name'] = 'bbm_dimmer'
                d['work_time'] = self.bbm_buf_bytes[self.BBM_DIMMER_WORKTIME_3] << 24 | \
                                 self.bbm_buf_bytes[self.BBM_DIMMER_WORKTIME_2] << 16 | \
                                 self.bbm_buf_bytes[self.BBM_DIMMER_WORKTIME_1] << 8 | \
                                 self.bbm_buf_bytes[self.BBM_DIMMER_WORKTIME_0]
                d['v_supl'] = "{:4.2f}".format(float(self.bbm_buf_bytes[self.BBM_DIMMER_V_SUP]) / self.BBMAGIC_VCC_DIVIDER)
                d['adv_time'] = self.bbm_buf[self.BBM_DIMMER_ADV_TIME] * 2
                d['chip_temp'] = self.bbm_buf[self.BBM_DIMMER_CHIP_TEMP]
                d['light'] = self.bbm_buf[self.BBM_RELAY_LIGHT]
                d['firmware'] = "{:x}.{:x}".format(self.bbm_buf[self.BBM_DIMMER_FIRM_1], self.bbm_buf[self.BBM_DIMMER_FIRM_0])
                d['dimer_ch0'] = self.bbm_buf[self.BBM_DIMMER_CH0]
                d['dimer_ch1'] = self.bbm_buf[self.BBM_DIMMER_CH1]
                d['dimer_ch2'] = self.bbm_buf[self.BBM_DIMMER_CH2]
                d['adc1'] = "{:4.3f}".format(float(self.bbm_buf[self.BBM_DIMMER_ADC_1_MSB] << 8 | \
                                 self.bbm_buf[self.BBM_DIMMER_ADC_1_LSB]) / 1000.0)

            elif device_type == self.BBMAGIC_M_LINUXDEVICE:
                d['type_name'] = 'bbm_linux'
                d['linux_timestamp'] = self.bbm_buf_bytes[self.BBM_LINUXLIB_TIMESTAMP_3] << 24 | \
                                 self.bbm_buf_bytes[self.BBM_LINUXLIB_TIMESTAMP_2] << 16 | \
                                 self.bbm_buf_bytes[self.BBM_LINUXLIB_TIMESTAMP_1] << 8 | \
                                 self.bbm_buf_bytes[self.BBM_LINUXLIB_TIMESTAMP_0]
                d['mac'] = self.buf2mac(self.bbm_buf, self.BBM_LINUXLIB_DEST_ADDR_5, self.BBM_LINUXLIB_DEST_ADDR_0)
                d['linux_lib_data'] = self.bbm_buf[self.BBM_LINUXLIB_DATA_2] << 16 | \
                                 self.bbm_buf[self.BBM_LINUXLIB_DATA_1] << 8 | \
                                 self.bbm_buf[self.BBM_LINUXLIB_DATA_0]
                d['linux_lib_version'] = "{:x}.{:x}".format(self.bbm_buf[self.BBM_LINUXLIB_VER_1], \
                                 self.bbm_buf[self.BBM_LINUXLIB_VER_0])

            else:
                d['type_name'] = "unknown"
                d['err_message'] = "Unknown device type"

        return d

    # Function: read data and convert to json format    
    def bbm_read_json(self):
        d = self.bbm_read_dict()
        js = json.dumps(d)

        return js
