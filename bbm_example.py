import json
from bbm_class import BBMagic
from time import sleep

print("")
print("    ***  BBMagic example   ***")
print("    *** hit Ctrl+C to stop ***")
print("")

bbm = BBMagic()
i = bbm.bbm_bt_lib_version()
print("BBMagic library version is {}".format(i))

i = bbm.bbm_bt_open()

while True:
	#js = bbm.bbm_read_json()
	#js = json.loads(js)
    js = bbm.bbm_read_dict()
    if js['result'] > 0 :
        print(js)

        ### example send to Domoticz dummy sensor
        # if js[type_name] == 'bbm_flood' && js['mac'] == 'C527FECE713C' : # check mac for BBMagic flood device
        #     idx = 123
        #      ip = '192.168.1.175'
        #      port = "8080"
        #     flood_flag = 'Off' if js['flood_flag'] else 'On'
        #     r = requests.get('https://' + ip + ':' + port + '/json.htm?type=command&param=udevice&idx={0}&nvalue=0&svalue={1}'.format(idx, flood_flag), auth=('user', 'pass'))
        #     print(r.status_code)
        #     print(r.text) 

    elif js['result'] == -1 :
        i = bbm.bbm_bt_close()
        exit(0)
    sleep(0.1)
