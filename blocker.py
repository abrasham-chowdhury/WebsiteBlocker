from time import sleep
from datetime import datetime
from sys import platform
import defaults

if platform == "linux" or platform == "darwin":
    hosts_path = "/etc/hosts"
elif platform == "win32":
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
else:
    raise Exception("Unsupported OS!")

_redirect = "127.0.0.1"

while True:
    if datetime(datetime.now().year, datetime.now().month, datetime.now().day, defaults.start_time) \
            < datetime.now() \
            < datetime(datetime.now().year, datetime.now().month, datetime.now().day, defaults.end_time):
        print("Work hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in defaults.website_list:
                if website in content:
                    pass
                else:
                    file.write(_redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in defaults.website_list):
                    file.write(line)
            file.truncate()
            print("Regular hours...")
    sleep(defaults.polling_rate)
