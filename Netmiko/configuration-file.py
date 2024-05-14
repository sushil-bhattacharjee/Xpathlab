from netmiko import ConnectHandler
from rich import print as rprint

device = {
    "device_type": "cisco_xe",
    "host": "10.1.10.22",
    "username": "sushil",
    "password": "sushil",
}




with ConnectHandler(**device) as conn:
        output1 = conn.send_config_from_file(config_file="ospf.cfg")
        print(output1)

show_commands = ["sh run | s router ospf", "sh run | s router bgp", "sh ip int bri", "sh run | s router isis"]

with ConnectHandler(**device) as conn:
    for command in show_commands:
        output = conn.send_command(command_string=command)
        print(output)