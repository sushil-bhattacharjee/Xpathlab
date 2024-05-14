from netmiko import ConnectHandler
from rich import print as rprint

my_device1 = {
    "device_type": "cisco_ios",
    "host": "10.1.10.29",
    #"host": "10.1.10.22",
    "username": "sushil",
    "password": "sushil",
}


#show_commands = ["sh ip int brief", "sh run | s mpls", "sh run vrf"]


with ConnectHandler(**my_device1) as conn:
    #for command in show_commands:
    #output = conn.send_command(command_string="show ip interface brief")
    #output = conn.send_command(command_string="sh run vrf")
     output1 = conn.send_config_from_file(config_file="R1-config.cfg")
     sh_run_bgp = conn.send_command(command_string="sh run | s router bgp")
     print()
     rprint(output1)
     print()
     print()
     rprint(f"sh run | router bgp", "\n" ,
            sh_run_bgp)
     print()
     print()
     #rprint(output1['platform'])
     print()
     print()