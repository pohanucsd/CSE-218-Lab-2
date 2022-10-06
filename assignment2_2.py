from Ultrasonic import Ultrasonic

if __name__ == "__main__":
    us = Ultrasonic()
    while True:
        try:
            cmd = input("Press A to measure distance.")
            if cmd.lower() == 'a':
                print('Measuring...')
                print(us.distance(), 'cm')
        except Exception:
            break
    
    print("Done")