args1 = ['ping', 'yandex.ru', '-c', '4']
args2 = ['ping', 'youtube.com', '-c', '4']

subproc_ping = subprocess.Popen(args1, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    print(line.decode('utf-8'), end='')

subproc_ping = subprocess.Popen(args2, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    print(line.decode('utf-8'), end='')