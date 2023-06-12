def host_range_ping(start, end, is_print=True):
    try:
        start_ip = ipaddress.ip_address(start)
        end_ip = ipaddress.ip_address(end)
        start_ip, end_ip = sorted((start_ip, end_ip))
    except Exception:
        print('Не верные параметры')
        return
    ips = []

    while start_ip <= end_ip:
        ips.append(start_ip)
        start_ip += 1

    return [i for i in host_ping(ips, is_print)]
