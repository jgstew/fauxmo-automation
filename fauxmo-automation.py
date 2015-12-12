
from fauxmo import *
from pyviera import VieraFinder
from wakeonlan import wol
#import requests

class vieria_handler(object):
    def __init__(self):
        self.vf = VieraFinder()
        self.tv = vf.get_viera()
        self.TV_WiFi_MAC = 'ff.ff.ff.ff.ff.ff'
        self.TV_LAN_MAC = 'ff.ff.ff.ff.ff.ff'

    def on(self):
        wol.send_magic_packet( self.TV_WiFi_MAC, self.TV_LAN_MAC )
        return 1==1

    def off(self):
        self.tv._sendkey('NRC_POWER-ONOFF')
        return 1==1

FAUXMOS = [
    ['tv', vieria_handler(), 45671]
    #,['sound', vizio_handler(), 45672]
]

