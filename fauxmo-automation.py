
from fauxmo import *
from pyviera import VieraFinder
from wakeonlan import wol

TV_WiFi_MAC = 'ff.ff.ff.ff.ff.ff'
TV_LAN_MAC = 'ff.ff.ff.ff.ff.ff'

FAUXMOS = [
    ['tv', vieria_handler(), 45671],
    ['sound', vizio_handler(), 45672],
]
