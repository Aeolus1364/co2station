import subprocess
import shlex
import tweepy


with open("keys", "r") as f:
    text = f.read()
    lines = text.splitlines()
    consumer_key = lines[0].split("consumer_key=")[1]
    consumer_secret = lines[1].split("consumer_secret=")[1]
    access_token = lines[2].split("access_token=")[1]
    access_token_secret = lines[3].split("access_token_secret=")[1]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


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
                api.update_status("Current CO2 level: " + co2)
                print(co2, hum, temp)


run_command("/home/pi/scd30_on_raspberry/scd30 -B -l 0")
