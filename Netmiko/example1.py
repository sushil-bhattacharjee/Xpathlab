from netmiko import ConnectHandler

my_device = {
    "device_type": "cisco_ios",
    "host": "10.1.10.29",
    "username": "sushil",
    "password": "sushil",
}

with ConnectHandler(**my_device) as conn:
    output = conn.send_command(command_string="show ip interface brief")
    print(output)

