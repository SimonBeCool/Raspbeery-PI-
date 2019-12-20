from gpiozero import LED, CPUTemperature
from time import sleep
import math

# LED variable configuration
is_normal = LED(17)
warning = LED(27)

# new CPU Libary
cpu = CPUTemperature()

if cpu.temperature < 60:
 is_normal.on()
 print("CPU Temperature is " + math.floor(cpu.temperature) + " °C")
 sleep(5)
 is_normal.off()

else: 
  warning.on()
  print("CPU Temperature is " + math.floor(cpu.temperature) + " °C")
  sleep(5)
  warning.off()
