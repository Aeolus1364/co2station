import subprocess
#import tweepy
import pickle
import datetime

"""
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
print('twitter initialized')
"""

print('starting')

co2_readings = []
temp_readings = []
hum_readings = []

times = []


def run_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    while True:
        try:
            output = process.stdout.readline()
            print(output)
            if output.decode("utf-8") == '' and process.poll() is not None:
                process.kill()
                break

            if output:
                text = output.strip().decode("utf-8").split()
                if text[0] == "CO2:":
                    co2 = text[1]
                    hum = text[4]
                    temp = text[7]

                    co2_readings.append(int(co2))
                    temp_readings.append(int(temp))
                    hum_readings.append(int(hum))
                    timestamp = datetime.datetime.now()
                    times.append(timestamp)
                    print("{0} at {1}".format(co2, timestamp.ctime()))

                    with open("data1", "wb+") as f:
                        pickle.dump([co2_readings, temp_readings, hum_readings, times], f)
                        print("done")

        except:
            pass

run_command("scd30_on_raspberry/scd30 -Bn -l 0 -w 2")
