######################################################################################
# Descirption: BBMagic class use the bbmagic_lib for support the MMBagic devices.
#              Site of BBMagic project is http://bbmagic.net
# author: Gabriel Zima (z1mEk)
# e-mail: gabriel.zima@wp.pl
# date: 2018-07-02
# compatibile version: 1.2
######################################################################################
# Future suport 1.4 library
# int bbm_bt_dimmer(unsigned char *dest_bd_addr, unsigned char *chan) ;
# int bbm_bt_relay_on(unsigned char *dest_bd_addr, unsigned char relays) ;
# int bbm_bt_relay_off(unsigned char *dest_bd_addr, unsigned char relays) ;
# int bbm_bt_open(int led_rx_pin, int led_tx_pin, int led_run_pin, int op_mode) ;
# ######################################################################################

import ctypes
from ctypes import *
bbm_bt_lib = ctypes.CDLL("./bbmagic_lib_1.2.so")

class BBMagic:
   
    #Function: open bt hci and starts bt scanning
    def bbm_bt_open(self, led_pin):
        return bbm_bt_lib.bbm_bt_open(led_pin)

    #Function: stops bt scanning and closes bt hci
    def bbm_bt_close(self):
        return bbm_bt_lib.bbm_bt_close()

    #Function: reads data from bbmagic modules
    def bbm_bt_read(self, bbm_data):
        bbm_buf = (c_byte * 23)()
        i = bbm_bt_lib.bbm_bt_read(byref(bbm_buf))
        bbm_data = bbm_buf
        return i

    #Function: returns version of bbm_bt library
    def bbm_bt_lib_version(self):
        return bbm_bt_lib.bbm_bt_lib_version()
