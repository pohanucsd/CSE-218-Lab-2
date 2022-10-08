from Led import RGBLed
from Ultrasonic import Ultrasonic

if __name__ == "__main__":
    rgb_led = RGBLed()
    ultrasonic = Ultrasonic()

    print("Press ctrl + c to stop the program")
    print("Start detecting...")
    while True:
        try:
            distance = int(ultrasonic.distance())
            if distance >= 100:
                distance = 100
            elif distance >= 1200:
                distance = 0
            rgb_led.changeDutyCycle(distance)
        except Exception:
            break
    
    print("Done")