from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "10.1.10.29",
    "username": "sushil",
    "password": "sushil",
}

my_commands = ["show version", "show ip int bri", "sh run | s router ospf"]

with ConnectHandler(**device) as conn:
    for command in my_commands:
        output = conn.send_command(command_string=command)
        print(output)