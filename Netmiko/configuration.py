from netmiko import ConnectHandler
from rich import print as rprint

device = {
    "device_type": "cisco_xe",
    "host": "10.1.10.29",
    "username": "sushil",
    "password": "sushil",
}


configuration_commands = [
    "router ospf 1",
    "router-id 10.1.10.29",
    "network 0.0.0.0 255.255.255.255 area 0"
]

with ConnectHandler(**device) as conn:
        output1 = conn.send_config_set(config_commands=configuration_commands)
        print(output1)

show_commands = ["sh run | s router ospf", "sh run | s router bgp", "sh ip int bri", "sh run | s router isis"]

with ConnectHandler(**device) as conn:
    for command in show_commands:
        output = conn.send_command(command_string=command)
        print(output)