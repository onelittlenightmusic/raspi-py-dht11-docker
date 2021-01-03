import RPi.GPIO as GPIO
import dht11
import time
import datetime
import os

if __name__ == "__main__":
	# initialize GPIO
	GPIO.setwarnings(True)
	GPIO.setmode(GPIO.BCM)

	pin = int(os.environ.get('DHT11_PIN_NUMBER'))
	interval = int(os.environ.get('DHT11_INTERVAL'))
	instance = dht11.DHT11(pin)
	try:
		while True:
			result = instance.read()
			if result.is_valid():
				print("Last valid input: " + str(datetime.datetime.now()))
				print("Temperature: %-3.1f C" % result.temperature)
				print("Humidity: %-3.1f %%" % result.humidity)
			time.sleep(interval)

	except KeyboardInterrupt:
		print("Cleanup")
		GPIO.cleanup()