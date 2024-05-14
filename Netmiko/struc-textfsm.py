from netmiko import ConnectHandler
from rich import print as rprint

device = {
    "device_type": "cisco_ios",
    "host": "10.1.10.29",
    "username": "sushil",
    "password": "sushil",
}

with ConnectHandler(**device) as conn:
    output = conn.send_command("sh version", use_textfsm=True)
    rprint(output[0]['serial'][0])
    rprint(output[0]['version'])

# genie doesn't work for me. need to troubleshoot

#with ConnectHandler(**device) as conn:
#    output1 = conn.send_command("sh version", use_genie=True)
#    rprint(output1)