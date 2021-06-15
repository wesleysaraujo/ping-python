import os
import time

with open('hosts.txt') as file:
    dump = file.read().splitlines()

    for host in dump:
        print('Verificando o host: ', host)
        print('-' * 60)
        response = os.system('ping -c 2 {}' .format(host))
        print(response)
        print('-' * 60)
        time.sleep(5)
