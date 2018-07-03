import ctypes
from ctypes import *
bbm_lib = ctypes.CDLL("./bbmagic_lib_1.2.so")

class BBMagic:
    def bbm_bt_open(self, led_pin):
        return bbm_lib.bbm_bt_open(led_pin)

    def bbm_bt_close(self):
        return bbm_lib.bbm_bt_close()

    def bbm_bt_read(self, bbm_data):
        bbm_buf = (c_byte * 23)()
        i = bbm_lib.bbm_bt_read(byref(bbm_buf))
        bbm_data = bbm_buf
        return i

    def bbm_bt_lib_version(self):
        return bbm_lib.bbm_bt_lib_version()
