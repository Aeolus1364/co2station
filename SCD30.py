import subprocess
import shlex


def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
    rc = process.poll()
    return rc


t = run_command("./scd30 -B -l 0")
print(t)
