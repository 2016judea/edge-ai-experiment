from gpiozero import LED
  
# GPIO header map: https://pinout.xyz/
led = LED(17) 

def turn_on_led(): 
    print("LED on!")
    led.on()
    
def turn_off_led(): 
    print("LED off!")
    led.off()