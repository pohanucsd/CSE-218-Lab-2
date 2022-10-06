import RPi.GPIO as GPIO
import time

PIN_TRIG = 'pin_trig'
PIN_ECHO = 'pin_echo'
TRIG = 31
ECHO = 29

class Ultrasonic:
    def __init__(self, trig=TRIG, echo=ECHO):
        self.pins = {PIN_TRIG: trig, PIN_ECHO: echo}
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location

        GPIO.setup(self.pins[PIN_TRIG], GPIO.OUT)
        GPIO.setup(self.pins[PIN_ECHO], GPIO.IN)
    
    def distance(self):
        self._emitUS()      # emit ultrasound
        dist = self._receiveUS()
        return dist

    '''
    Emit ultrasound
    '''
    def _emitUS(self):
        GPIO.output(TRIG, 0)
        time.sleep(0.000002)
        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)

    '''
    Get ultrasound signal and calculate distance
    '''
    def _receiveUS(self):
        while GPIO.input(ECHO) == 0:
            pass                            
        time_start = time.time()
        while GPIO.input(ECHO) == 1:
            pass
        time_end = time.time()
        during = time_end - time_start
        return during * 340 / 2 * 100


    def __del__(self):
        GPIO.cleanup()