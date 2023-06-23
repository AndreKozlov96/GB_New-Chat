import subprocess
from chardet import detect

args_yandex = ['ping', 'yandex.ru']
args_youtube = ['ping', 'youtube.com']

# ping for YANDEX.RU

subproc_ping = subprocess.Popen(args_yandex, stdout=subprocess.PIPE)
print('\n--------------YANDEX--------------', end='')
for line in subproc_ping.stdout:
    detected = detect(line)
    encoded = detected['encoding']
    print(line.decode(encoded), end='')

# ping for YOUTUBE.COM

subproc_ping = subprocess.Popen(args_youtube, stdout=subprocess.PIPE)
print('\n--------------YOUTUBE--------------', end='')
for line in subproc_ping.stdout:
    detected = detect(line)
    encoded = detected['encoding']
    print(line.decode(encoded), end='')
