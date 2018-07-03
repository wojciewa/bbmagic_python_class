import ctypes
from ctypes import *
bbm_lib = ctypes.CDLL("./bbmagic_lib_1.2.so")

def bbm_bt_open(led_pin):
    return bbm_lib.bbm_bt_open(led_pin)

def bbm_bt_close():
    return bbm_lib.bbm_bt_close()

def bbm_bt_read(bbm_data):
    bbm_buf = (c_byte * 23)()
    i = bbm_lib.bbm_bt_read(byref(bbm_buf))
    bbm_data = bbm_buf
    return i

def bbm_bt_lib_version():
    return bbm_lib.bbm_bt_lib_version()

i = bbm_bt_lib_version()
print "bbm library version is {0}".format(i)

i = bbm_bt_open(17)
bbm_buf = ''

while True:
    data_length = bbm_bt_read(bbm_buf)
    if data_length > 0 :
        print data_length
        print bbm_buf[4]
