# fauxmo-automation
Home automation through Belkin WeMo emulation, which enables devices to be turned off and on with Amazon Echo (Alexa)

Emulating a Belkin WeMo switch requires: https://github.com/makermusings/fauxmo

An emulated switch must have a way to turn the device off and on. It might be possible to do something else when the switch is turned off or on, but the only input option is off or on.


# Devices:

## Panasonic Viera TV

Can be turned off using https://github.com/tomokas/pyviera

```python
    from pyviera import VieraFinder
    vf = VieraFinder()
    tv = vf.get_viera()
    tv._sendkey('NRC_POWER-ONOFF')
```

Should be able to be turned on using Wake-On-LAN
- https://pypi.python.org/pypi/wakeonlan/0.2.2
- https://github.com/remcohaszing/pywakeonlan

```python
    from wakeonlan import wol
    wol.send_magic_packet('ff.ff.ff.ff.ff.ff', '00-00-00-00-00-00')
```
Note: the `('ff.ff.ff.ff.ff.ff', '00-00-00-00-00-00')` should be changed to the TV's actual MAC address, also, the TV has both a WiFi MAC & a LAN MAC. WoL packets should be sent to both at the same time.


## Visio Soundbar

Shoud be controllable through:
- https://github.com/jterrace/pyharmony
- http://support.logitech.com/en_us/product/harmony-link

# References:
- https://github.com/makermusings/fauxmo
- http://www.makermusings.com/2015/07/18/virtual-wemo-code-for-amazon-echo/
- https://github.com/tomokas/pyviera
- https://github.com/petele/pyharmony/
- http://www.makermusings.com/2015/07/13/amazon-echo-and-home-automation/
