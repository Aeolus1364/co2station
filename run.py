import subprocess
import datetime
import pickle

co2_readings = []
temp_readings = []
humid_readings = []
times = []

def run_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            text = output.strip().decode('utf-8').split()
            if text[0] == 'CO2:':
                co2 = text[1]
                humid = text[4]
                temp = text[7]

                co2_readings.append(int(co2))
                humid_readings.append(float(humid))
                temp_readings.append(float(temp))
                timestamp = datetime.datetime.now()
                times.append(timestamp)

                print(text[1], text[4], text[7], timestamp)

                with open('data', 'wb+') as f:
                    pickle.dump([co2_readings, humid_readings, temp_readings, times], f)

run_command('scd30_on_raspberry/scd30 -Bn -l 0 -w 60')
