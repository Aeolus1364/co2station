import subprocess
import shlex


def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            text = output.strip().decode("utf-8").split()
            if text[0] == "CO2:":
                co2 = text[1]
                hum = text[4]
                temp = text[7]
                print(co2, hum, temp)


run_command("./scd30 -B -l 0")
