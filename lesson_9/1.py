def host_ping(hosts, is_print=True):
    for host in hosts:
        try:
            ip = ipaddress.ip_address(host)
        except Exception:
            ip = host
        command = ['ping', param, '1', str(ip)]
        response = subprocess.run(command, shell=is_win, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        mes = 'Узел доступен' if response.returncode == 0 else 'Узел не доступен'
        if is_print:
            yield print(f'{ip}: {mes}')
        else:
            key = 'Reachable' if response.returncode == 0 else 'Unreachable'
            yield {key: ip}
