import subprocess
import shlex
import tweepy
import pickle


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

readings = []

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        try:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                text = output.strip().decode("utf-8").split()
                if text[0] == "CO2:":
                    co2 = text[1]
                    hum = text[4]
                    temp = text[7]

                    readings.append(int(co2))

                    total = 0
                    for i in readings:
                        total += i
                    avg = total / len(readings)

                    print("{0} AVG {1}".format(co2, round(avg, 2)))

                    with open("data", "w+") as f:
                        pickle.dump(readings, f)

        except:
            pass

run_command("/home/pi/scd30_on_raspberry/scd30 -Bn -l 0")
