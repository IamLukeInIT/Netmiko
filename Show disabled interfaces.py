from netmiko import ConnectHandler
from getpass import getpass

user = "#"
password = getpass('Password: ')


SW0_4 = {
    'device_type': 'cisco_ios',
    'host': '10.10.5.11',
    'username': user,
    'password': password,
}

SW0_5 = {
    'device_type': 'cisco_ios',
    'host': '10.10.5.15',
    'username': user,
    'password': password,
}

SW0_8 = {
    'device_type': 'cisco_ios',
    'host': '10.10.5.19',
    'username': user,
    'password': password,
}

#next switches...

#commands
sh_host = 'show running-config | include hostname'
sh_int = 'show interface status | include disabled'

switches = [SW0_4, SW0_5, SW0_8,...]

for switch in switches:
    with ConnectHandler(**switch) as net_connect:
        output_hostname = net_connect.send_command(sh_host)
        output_interfaces = net_connect.send_command(sh_int)

        print()
        print(output_hostname)
        print(output_interfaces)
        print()

net_connect.disconnect()
print('Close sessions...')