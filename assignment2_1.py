from Led import RGBLed

if __name__ == "__main__":
    rgb_led = RGBLed()
    while True:
        try:
            dc = int(input("Assign new duty of cycle here: "))
            rgb_led.changeDutyCycle(dc)
        except Exception:
            break
    
    print("Done")