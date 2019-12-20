# This script was coded by Simon Bucher for learning Python

from gpiozero import LED, CPUTemperature
from time import sleep
import math
import logging

#Add new logging libary for better performance then use print()
log = logging.getLogger()
console = logging.Streamhandler()

# Add handler of logging 
log.addHandler(console)

#Add LED variable configuration
is_normal = LED(17)
warning = LED(27)

#Add new cpu libary
cpu = CPUTemperature()

if cpu.temperature < 60:
 is_normal.on()
 log.warn('CPU has ' + math.floor(cpu.temperature) + ' °C')
 sleep(5)
 is_normal.off()

else: 
  warning.on()
  log.warn('CPU has ' + math.floor(cpu.temperature) + ' °C')
  sleep(5)
  warning.off()
