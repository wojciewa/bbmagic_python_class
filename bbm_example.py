from bbm_class import BBMagic # import python BBMagic class 
from time import sleep

print("")
print("    ***  BBMagic example   ***")
print("    *** hit Ctrl+C to stop ***")
print("")

bbm = BBMagic() # initialize BBMagic class
i = bbm.bbm_bt_lib_version() # get BBMagic library version
print("BBMagic library version is {}".format(i)

i = bbm.bbm_bt_open(17) # open bt hci and starts bt scanning
if i != 0:
    print("some errors occured")
    exit(0)

while True:
    js = bbm.bbm_bt_read_json() # get object from scanning line
    if js['result'] > 0 :
        ### example print to console
        print(js['mac'] + " | " + str(js['type']) + " | " + str(js['adv_time'])  + " | " + str(js['v_supl']) + "V | " + str(js['rssi']) + "dBm | " + str(js['flood_alert_flag']))
        ### example print object (json) to console
        # print(js)
        ### example send to Domoticz dummy sensor
        # if js['mac'] == 'C527FECE713C' : # check mac for BBMagic flood device
        #     idx = 123
        #     flood_flag = 'Off' if js['flood_flag'] else 'On'
        #     r = requests.get('https://<ip_domoticz>:<domoticz_port>/json.htm?type=command&param=udevice&idx={0}&nvalue=0&svalue={1}'.format(idx, flood_flag), auth=('user', 'pass'))
        #     print(r.status_code)
    elif js['result'] == -1 :
        i = bbm.bbm_bt_close() # tops bt scanning and closes bt hci
        exit(0)
    sleep(1)
