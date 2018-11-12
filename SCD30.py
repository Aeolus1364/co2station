import subprocess


def read():
    result = subprocess.run(['/home/pi/scd30_on_raspberry/scd30', '-SB'], stdout=subprocess.PIPE)
    decoded = result.stdout.decode('utf-8')
    data = decoded.split()
    co2, humidity, temperature = None, None, None
    for n, w in enumerate(data):
        m = w.lower()
        if "co2" in m:
            co2 = int(data[n + 1])
        elif "humidity" in m or "humdity" in m:
            humidity = float(data[n + 1])
        elif "temperature" in m:
            temperature = float(data[n + 1])

    return co2, humidity, temperature
