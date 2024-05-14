from netmiko import ConnectHandler

my_device1 = {
    "device_type": "cisco_ios",
    "host": "10.1.10.29",
    #"host": "10.1.10.22",
    "username": "sushil",
    "password": "sushil",
}

my_device2 = {
    "device_type": "cisco_ios",
    #"host": "10.1.10.29",
    "host": "10.1.10.28",
    "username": "sushil",
    "password": "sushil",
}

show_commands = ["sh ip int brief", "sh run | s mpls", "sh run vrf"]

with ConnectHandler(**my_device1) as conn:
    for command in show_commands:
    #output = conn.send_command(command_string="show ip interface brief")
    #output = conn.send_command(command_string="sh run vrf")
     output1 = conn.send_command(command_string=command)
     print()
     print(output1)