
from fauxmo import *
from pyviera import VieraFinder
from wakeonlan import wol
import requests

TV_WiFi_MAC = 'ff.ff.ff.ff.ff.ff'
TV_LAN_MAC = 'ff.ff.ff.ff.ff.ff'

class vieria_handler(object):
    def __init__(self):
        pass

    def on(self):
        
        return 1==1

    def off(self):
        
        return 1==1

FAUXMOS = [
    ['tv', vieria_handler(), 45671]
    #,['sound', vizio_handler(), 45672]
]

