import subprocess

def run_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            text = output.strip().decode('utf-8').split()
            if text[0] == 'CO2:':
                print(text[1], text[4], text[7])

run_command('scd30_on_raspberry/scd30 -Bn -l 0 -w 5')
