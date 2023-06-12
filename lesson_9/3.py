def host_range_ping_tab(start, end):
    print(tabulate(host_range_ping(start, end, is_print=False), headers='keys'))


if __name__ == '__main__':
    list(host_ping(('192.168.0.1', 'ya.ru', 'trails')))
    host_range_ping('192.168.0.1', '192.168.0.3')
    host_range_ping_tab('192.168.0.1', '192.168.0.3')