from netmiko import ConnectHandler
from rich import print as rprint

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

#show_commands = ["sh ip int brief", "sh run | s mpls", "sh run vrf"]
commands = [
     "router ospf 1", 
     "router-id 10.1.1.1", 
     "network 10.1.10.0 0.0.0.255 area 0"
     ]

with ConnectHandler(**my_device1) as conn:
    #for command in show_commands:
    #output = conn.send_command(command_string="show ip interface brief")
    #output = conn.send_command(command_string="sh run vrf")
     output1 = conn.send_config_set(config_commands=commands)
     sh_run_ospf = conn.send_command(command_string="sh run | s router ospf")
     print()
     rprint(output1)
     print()
     print()
     rprint(sh_run_ospf)
     print()
     print()
     #rprint(output1['platform'])
     print()
     print()