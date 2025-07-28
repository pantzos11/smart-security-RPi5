import RPi.GPIO as GPIO
import time

KEY_PIN = 17  # GPIO17 (Pin 11)

GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(KEY_PIN) == GPIO.HIGH:
            print("🔓 Συναγερμός απενεργοποιημένος (OFF)")
        else:
            print("🔒 Συναγερμός ενεργοποιημένος (ON)")
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
