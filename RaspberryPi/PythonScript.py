from gpiozero import Servo,LED
from time import sleep

ledpinG= LED(12)
ledpinR= LED(13)
#servo=AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0025)
servo=Servo(18)

def license_plate_detected():
        #open gate
        #90->0->-90
	  #1->0->-1
        #servo.value=1
        for i in range(1,11):
                servo.value=i*0.1
                sleep(0.1)
        #glow green
        ledpinG.on()
        
        #switch off red
        ledpinR.off()
        
        sleep(5)#sleep or wait

        #close gate
        for i in range(1,11):
                servo.value=1-(i*0.1)
                sleep(0.1)
        #servo.value=0
        
        #switch on red
        ledpinR.on()
        
        #switch off green
        ledpinG.off()
        
        sleep(5)

license_plate_detected()
