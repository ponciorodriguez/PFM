# This file is executed on every boot (including wake-boot from deepsleep)

import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'calaestancia'
password = 'Catieta1'

station = network.WLAN(network.STA_IF)

station.active(True)

station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
led = Pin(2, Pin.OUT)