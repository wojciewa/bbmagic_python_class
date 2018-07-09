


#ifndef __BBMAGIC_LIB_H
#define __BBMAGIC_LIB_H

#ifdef __cplusplus
extern "C" {
#endif

//-BBMagic device types
//---------------------------------------------------------------------------------------------
#define BBMAGIC_M_METEO                 1       //-BBMagic meteo module: T, RH, Light
#define BBMAGIC_M_MOTION                2
#define BBMAGIC_M_BUTTON                3
#define BBMAGIC_M_FLOOD                 4
#define BBMAGIC_M_MAGNETO               5
#define BBMAGIC_M_LINUXDEVICE           6
#define BBMAGIC_M_RELAY                 20
#define BBMAGIC_M_DIMMER                21


//-BBMagic Lib buffer offsets for all devices
//---------------------------------------------------------------------------------------------
//-BBMagic device ID
#define BBMAGIC_DEVICE_TYPE		    	4
//-Bluetooth device address
#define BBMAGIC_DEVICE_ADDR_5           16
#define BBMAGIC_DEVICE_ADDR_4           17
#define BBMAGIC_DEVICE_ADDR_3           18
#define BBMAGIC_DEVICE_ADDR_2           19
#define BBMAGIC_DEVICE_ADDR_1           20
#define BBMAGIC_DEVICE_ADDR_0           21
//-Bluetooth Radio Sugnal Strength Indicator
#define BBMAGIC_DEVICE_RSSI             22
//-Divider to calculate module supply voltage in Volts
#define BBMAGIC_VCC_DIVIDER             71.0

//-BBMagic Lib buffer offsets
//---------------------------------------------------------------------------------------------
//-BBMagic METEO module
#define BBM_METEO_WORKTIME_0            0
#define BBM_METEO_WORKTIME_1		    1
#define BBM_METEO_WORKTIME_2		    2
#define BBM_METEO_WORKTIME_3            3
#define BBM_METEO_V_SUP			        5
#define BBM_METEO_ADV_TIME              6
#define BBM_METEO_DIN_STATE		        7
#define BBM_METEO_TEMPER_MSB		    8
#define BBM_METEO_TEMPER_LSB		    9
#define BBM_METEO_HUM		            10
#define BBM_METEO_LIGHT   			    11
#define BBM_METEO_ADC_1_MSB             12
#define BBM_METEO_ADC_1_LSB             13
#define BBM_METEO_ADC_2_MSB             14
#define BBM_METEO_ADC_2_LSB             15

//-BBMagic BUTTON module
#define BBM_BUTTON_SIGN_0               0
#define BBM_BUTTON_SIGN_1               1
#define BBM_BUTTON_SIGN_2		        2
#define BBM_BUTTON_SIGN_3               3
#define BBM_BUTTON_V_SUP			    5
#define BBM_BUTTON_BUTTON_FUNCTION      7
#define BBM_BUTTON_INPUT_PINS           8
#define BBM_BUTTON_CHIP_TEMP            9
#define BBM_BUTTON_LIGHT			    10
#define BBM_BUTTON_FIRM_1               14
#define BBM_BUTTON_FIRM_0               15
#define BBM_BUTTON_FN_SINGLE_CLICK      1
#define BBM_BUTTON_FN_DOUBLE_CLICK      2
#define BBM_BUTTON_FN_HOLDING           3

//-BBMagic MOTION module
#define BBM_MOTION_WORKTIME_0           0
#define BBM_MOTION_WORKTIME_1           1
#define BBM_MOTION_WORKTIME_2           2
#define BBM_MOTION_WORKTIME_3           3
#define BBM_MOTION_V_SUP			    5
#define BBM_MOTION_FLAGS	            7
#define BBM_MOTION_CHIP_TEMP            8
#define BBM_MOTION_LIGHT			    9
#define BBM_MOTION_ADC_1_MSB            10
#define BBM_MOTION_ADC_1_LSB            11
#define BBM_MOTION_ADC_2_MSB            12
#define BBM_MOTION_ADC_2_LSB            13
#define BBM_MOTION_FIRM_1               14
#define BBM_MOTION_FIRM_0               15
#define BBM_MOTION_ALERT_MASK           0x80

//-BBMagic FLOOD module
#define BBM_FLOOD_WORKTIME_0    		0
#define BBM_FLOOD_WORKTIME_1	       	1
#define BBM_FLOOD_WORKTIME_2            2
#define BBM_FLOOD_WORKTIME_3            3
#define BBM_FLOOD_V_SUP		           	5
#define BBM_FLOOD_ADV_TIME              6
#define BBM_FLOOD_ALERT_FLAGS		    7
#define BBM_FLOOD_CHIP_TEMP             8
#define BBM_FLOOD_FIRM_1                14
#define BBM_FLOOD_FIRM_0                15
#define BBM_FLOOD_ALERT_MASK            0x01

//-BBMagic MAGNETO module
#define BBM_MAGNETO_WORKTIME_0    		0
#define BBM_MAGNETO_WORKTIME_1	       	1
#define BBM_MAGNETO_WORKTIME_2          2
#define BBM_MAGNETO_WORKTIME_3          3
#define BBM_MAGNETO_V_SUP		        5
#define BBM_MAGNETO_ADV_TIME            6
#define BBM_MAGNETO_FLAGS		        7
#define BBM_MAGNETO_CHIP_TEMP           8
#define BBM_MAGNETO_LIGHT               9
#define BBM_MAGNETO_ADC_1_MSB           10
#define BBM_MAGNETO_ADC_1_LSB           11
#define BBM_MAGNETO_ADC_2_MSB           12
#define BBM_MAGNETO_ADC_2_LSB           13
#define BBM_MAGNETO_FIRM_1              14
#define BBM_MAGNETO_FIRM_0              15
#define BBM_MAGNETO_MAGNET_MASK         0x80
#define BBM_MAGNETO_IN_0_BIT            0x01
#define BBM_MAGNETO_IN_1_BIT            0x02
#define BBM_MAGNETO_IN_2_BIT            0x04
#define BBM_MAGNETO_IN_3_BIT            0x08

//-LINUX DEVICE with BBM LIB
#define BBM_LINUXLIB_TIMESTAMP_0   		0
#define BBM_LINUXLIB_TIMESTAMP_1       	1
#define BBM_LINUXLIB_TIMESTAMP_2        2
#define BBM_LINUXLIB_TIMESTAMP_3        3
#define BBM_LINUXLIB_DEST_ADDR_5        5
#define BBM_LINUXLIB_DEST_ADDR_4        6
#define BBM_LINUXLIB_DEST_ADDR_3        7
#define BBM_LINUXLIB_DEST_ADDR_2        8
#define BBM_LINUXLIB_DEST_ADDR_1        9
#define BBM_LINUXLIB_DEST_ADDR_0        10
#define BBM_LINUXLIB_DATA_0             11
#define BBM_LINUXLIB_DATA_1             12
#define BBM_LINUXLIB_DATA_2             13
#define BBM_LINUXLIB_VER_1              14
#define BBM_LINUXLIB_VER_0              15

//-BBMagic RELAY module
#define BBM_RELAY_WORKTIME_0		    0
#define BBM_RELAY_WORKTIME_1            1
#define BBM_RELAY_WORKTIME_2		    2
#define BBM_RELAY_WORKTIME_3            3
#define BBM_RELAY_V_SUP			        5
#define BBM_RELAY_ADV_TIME              6
#define BBM_RELAYS_STATE		        7
#define BBM_RELAY_CHIP_TEMP	            8
#define BBM_RELAY_LIGHT	                9
#define BBM_RELAY_ADC_1_MSB             10
#define BBM_RELAY_ADC_1_LSB             11
#define BBM_RELAY_ADC_2_MSB             12
#define BBM_RELAY_ADC_2_LSB             13
#define BBM_RELAY_FIRM_1                14
#define BBM_RELAY_FIRM_0                15
#define BBM_RELAY_0                     1
#define BBM_RELAY_1                     2
#define BBM_RELAY_2                     4
#define BBM_RELAY_3                     8

//-BBMagic DIMMER module
#define BBM_DIMMER_WORKTIME_0           0
#define BBM_DIMMER_WORKTIME_1           1
#define BBM_DIMMER_WORKTIME_2           2
#define BBM_DIMMER_WORKTIME_3           3
#define BBM_DIMMER_V_SUP			    5
#define BBM_DIMMER_ADV_TIME             6
#define BBM_DIMMER_CHIP_TEMP	        7
#define BBM_DIMMER_LIGHT	            8
#define BBM_DIMMER_CH0		            9
#define BBM_DIMMER_CH1                  10
#define BBM_DIMMER_CH2                  11
#define BBM_DIMMER_ADC_1_MSB            12
#define BBM_DIMMER_ADC_1_LSB            13
#define BBM_DIMMER_FIRM_1               14
#define BBM_DIMMER_FIRM_0               15

//---------------------------------------------------

#define BBLIB_FRAME_SIZE                23
#define BBM_BT_ADDR_SIZE                6

//*******************************************************************************************
//-Public Function: open bt hci and starts bt scanning
//LED pins: 2-27 - number of Raspberry Pi pin with LED connected. ; <2 and >27 - no LED indication
//-led_rx_pin - for rx signaling
//-led_tx_pin - for tx signaling
//-led_run_pin - for working signaling
//-op_mode: console messages: 0-off ; !=0-on
//returning values:
// 0 - bbmagic bluetooth opened
// !=0 - some errors occured
//*******************************************************************************************
    int bbm_bt_open(int led_rx_pin, int led_tx_pin, int led_run_pin, int op_mode) ;

//*******************************************************************************************
//-Public Function: stops bt scanning and closes bt hci
//returning values:
// 0 - bbmagic bluetooth closed
// !=0 - some errors occured
//*******************************************************************************************
    int bbm_bt_close(void) ;

//*******************************************************************************************
//-Public Function: reads data from bbmagic modules
//gets pointer to the buffer ; buffer size should be >= BBLIB_FRAME_SIZE
//returning values:
// 0 : no bt data arrived
// >0 : bytes red
//-1 : user break (ctrl+C)
//-2 : data red ; not HCI event pocket
//-4 : red HCI event pocket ; not LE Advertising Report event
//-6 : red HCI event pocket LE Advertising Report event ; not Manufacturer specific data
//-8 : reserved for: wrong Manufacturer ID
//-10 : authentication error
//-12 : other error
//*******************************************************************************************
    int bbm_bt_read(unsigned char *bbm_data) ;

//*******************************************************************************************
//-Public Function: turns on bbm relays
//- dest_bd_addr - Bluetooth MAC addr of destination device - 6 bytes MSB to LSB
//- relays - relays to switch on ; ; BBM_RELAY_0..BBM_RELAY_3
//ret val:
// 0 : sended ok
// <0 : sending error
//*******************************************************************************************
    int bbm_bt_relay_on(unsigned char *dest_bd_addr, unsigned char relays) ;

//*******************************************************************************************
//-Public Function: turns off selected relays
//- dest_bd_addr - Bluetooth MAC addr of destination device - 6 bytes MSB to LSB
//- relays - relays to switch off ; BBM_RELAY_0..BBM_RELAY_3
//ret val:
// 0 : sended ok
// <0 : sending error
//*******************************************************************************************
    int bbm_bt_relay_off(unsigned char *dest_bd_addr, unsigned char relays) ;

//*******************************************************************************************
//-Public Function: sets bbm dimmer channels
//- dest_bd_addr - Bluetooth MAC addr of destination device - 6 bytes MSB to LSB
//- chan - pointer to three elements table ; chan[0].. chan[3] - channels values
//returning values:
// 0 : sended ok
// <0 : sending error
//*******************************************************************************************
    int bbm_bt_dimmer(unsigned char *dest_bd_addr, unsigned char *chan) ;

//*******************************************************************************************
//-Public Function: returns version of bbm_bt library
//returning values:
// int - bbm_bt_lib version
//*******************************************************************************************
    int bbm_bt_lib_version(void) ;

//*******************************************************************************************
//-Public Function: gets 6 bytes of Bluetooth device address and stores it in unsigned char *bt_addr
//returning values:
// 6 - 6 bytes address read ok
// <0 - addres read error
// -2 - BBM BT not opened - call bbm_bt_open(..) first
//*******************************************************************************************
    int bbm_bt_myaddr_get(unsigned char *bt_addr) ;

#endif  //-ndef __BBMAGIC_LIB_H
