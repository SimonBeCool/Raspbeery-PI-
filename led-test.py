from gpiozero import LED
from time import sleep

blau = LED(17) #Blaue LED
gelb = LED(27) #Gelbe LED

blau.on()
sleep(5)
blau off()

gelb.on()
sleep(5)
gelb.off()

