from bbm_class import BBMagic
from time import sleep

bbm = BBMagic()
i = bbm.bbm_bt_lib_version()
print "BBMagic library version is {0}".format(i)

i = bbm.bbm_bt_open(17)

while True:
    js = bbm.bbm_bt_read_json()
    if js['result'] > 0 :
        print js['mac'] + " | " + str(js['type'])  + " | " + str(js['v_supl']) + "V | " + str(js['rssi']) + "dBm | " + str(js['flood_alert_flag'])
        #print js
    elif js['result'] == -1 :
        i = bbm.bbm_bt_close()
        exit(0)
    sleep(0.1)
