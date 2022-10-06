import RPi.GPIO as GPIO

class RGBLed:
    def __init__(self, R = 11, G = 12, B = 13):
        self.pins = {'pin_R': R, 'pin_G': G, 'pin_B': B}
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
        for i in self.pins:
            GPIO.setup(self.pins[i], GPIO.OUT)   # Set pins' mode is output
            GPIO.output(self.pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led
        
        self.p_R = GPIO.PWM(self.pins['pin_R'], 2000)
        self.p_G = GPIO.PWM(self.pins['pin_G'], 3000)
        self.p_B = GPIO.PWM(self.pins['pin_B'], 4000)
        
        # 100: Led light off, 0 Led light max
        self.p_R.start(100)
        self.p_G.start(100)
        self.p_B.start(100)
    
    def __del__(self):
        GPIO.cleanup()
    
    def changeDutyCycle(self, dc):
        self.p_R.ChangeDutyCycle(dc)
        self.p_G.ChangeDutyCycle(dc)
        self.p_B.ChangeDutyCycle(dc)