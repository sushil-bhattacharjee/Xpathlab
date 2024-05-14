from netmiko import ConnectHandler

my_device1 = {
    "device_type": "cisco_ios",
    "host": "10.1.10.28",
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

with ConnectHandler(**my_device1) as conn:
    #output = conn.send_command(command_string="show ip interface brief")
    #output = conn.send_command(command_string="sh run vrf")
    #output1 = conn.send_command(command_string="sh run | s mpls")
    output1 = conn.send_command(command_string="sh run | s router ospf")
    output_bgp = conn.send_command(command_string="sh run | s router bgp")
print()
print(output1)
print()
print(output_bgp)

print(f"Output for the router= {my_device2['host']}")

with ConnectHandler(**my_device2) as conn:
    #output = conn.send_command(command_string="show ip interface brief")
    #output2 = conn.send_command(command_string="sh run vrf")
    #output2 = conn.send_command(command_string="sh run | s mpls")
    output2_bgp = conn.send_command(command_string="sh run | s router bgp")
print(output2_bgp)