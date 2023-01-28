from netmiko import ConnectHandler
from getpass import getpass

user = '#'
password = getpass('Password: ')

sw_1 = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.10',
    'username': user,
    'password': getpass(),
}

cmd = "show mac address-table int"
interfaces = [f'g1/0/{i}' for i in range (1,49)]

with ConnectHandler(**sw_1) as net_connect:
    for interface in interfaces:
        output = net_connect.send_command(cmd + interface)

        print()
        print(output)
        print()

net_connect.disconnect()
print("CLose session")
