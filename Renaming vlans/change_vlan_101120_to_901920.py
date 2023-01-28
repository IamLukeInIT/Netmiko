from netmiko import ConnectHandler
from getpass import getpass
from colorama import Fore, Back, Style

user = "#"
password = getpass('Password: ')


SW9_CORE = {
    'device_type': 'cisco_ios',
    'host': '10.19.5.1',
    'username': user,
    'password': password,
}

SW9_1 = {
    'device_type': 'cisco_ios',
    'host': '10.19.5.11',
    'username': user,
    'password': password,
}

SW9_2 = {
    'device_type': 'cisco_ios',
    'host': '10.19.5.12',
    'username': user,
    'password': password,
}


#command SW9_CORE
with open('vlan901920_sw9_core.txt') as f:
    cmd_sw9_core = f.read().splitlines()

switches = [SW9_CORE]
print(Fore.GREEN + 'SW9_CORE')
print(Style.RESET_ALL)

for switch in switches:
    net_connect = ConnectHandler(**SW9_CORE)
    output = net_connect.send_config_set(cmd_sw9_core)

    print()
    print(output)
    print()

#command SW9_1
with open('vlan901920_sw9_1.txt') as f:
    cmd_sw9_1 = f.read().splitlines()

switches = [SW9_1]
print(Fore.GREEN + 'SW9_1')
print(Style.RESET_ALL)

for switch in switches:
    net_connect = ConnectHandler(**SW9_1)
    output = net_connect.send_config_set(cmd_sw9_1)

    print()
    print(output)
    print()

#command SW9_2
with open('vlan901920_sw9_2.txt') as f:
    cmd_sw9_2 = f.read().splitlines()

switches = [SW9_2]
print(Fore.GREEN + 'SW9_2')
print(Style.RESET_ALL)

for switch in switches:
    net_connect = ConnectHandler(**SW9_2)
    output = net_connect.send_config_set(cmd_sw9_2)

    print()
    print(output)
    print()

#next switches...

#closed sessions all
net_connect.disconnect()
print('Close SSH sesions...')