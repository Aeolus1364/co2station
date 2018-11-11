import subprocess


def read():
    result = subprocess.run(['exec /home/pi/scd30_on_raspberry/scd30', '-S'], stdout=subprocess.PIPE)
    decoded = result.stdout.decode('utf-8')
    data = decoded.split()[-8:]
    co2 = data[0]
    humidity = data[3]
    temperature = data[6]
    return co2, humidity, temperature
