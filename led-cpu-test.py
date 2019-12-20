from gpiozero import LED, CPUTemperature
from time import sleep

# LED variable configuration
is_normal = LED(17)
warning = LED(27)

# new CPU Libary
cpu = CPUTemperature()

if cpu.temperature < 60:
 is_normal.on()
 sleep(5)
 is_normal.off()

else: 
  warning.on()
  sleep(5)
  warning.off()
