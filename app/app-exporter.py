from flask import Flask
import dht11
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

pin = int(os.environ.get('DHT11_PIN_NUMBER'))
interval = int(os.environ.get('DHT11_INTERVAL'))
prefix = os.environ.get('DHT11_PREFIX')
instance = dht11.DHT11(pin)

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    dht11_data = ""
    result = instance.read()
    if result.is_valid():
        dht11_data = f"""{prefix}_temperature {result.temperature}
{prefix}_humidity {result.humidity}"""

    return f"{dht11_data}", 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    app.run(host='0.0.0.0')
