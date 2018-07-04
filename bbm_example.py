from bbm_class import BBMagic
from time import sleep

bbm = BBMagic()
i = bbm.bbm_bt_lib_version()
print "BBMagic library version is {0}".format(i)

i = bbm.bbm_bt_open(17)

while True:
    js = bbm.bbm_bt_read_json()
    if js['result'] > 0 :
        ### example print to console
        print js['mac'] + " | " + str(js['type']) + " | " + str(js['adv_time'])  + " | " + str(js['v_supl']) + "V | " + str(js['rssi']) + "dBm | " + str(js['flood_alert_flag'])
        ### example print object (json) to console
        # print js
        ### example send to Domoticz dummy sensor
        # idx = 123
        # flood_flag = 'Off' if js['flood_flag'] else 'On'
        # r = requests.get('https://<ip_domoticz>:<domoticz_port>/json.htm?type=command&param=udevice&idx={0}&nvalue=0&svalue={1}'.format(idx, flood_flag), auth=('user', 'pass'))
        # print r.status_code
    elif js['result'] == -1 :
        i = bbm.bbm_bt_close()
        exit(0)
    sleep(0.1)
