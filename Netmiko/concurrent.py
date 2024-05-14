from inv import DEVICES
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor

#Serial connection
#for device in DEVICES:
#    print(device["host"])
#    with ConnectHandler(
#        device_type="cisco_xe",
#        host=device["host"],
#        username="sushil",
#        password="sushil"
#    ) as conn:
#        output = conn.send_command("sh run | s router ospf")
#    print(output)

#Concurrent connection
def send_cmd_to_device(device):
    with ConnectHandler(
        device_type="cisco_xe",
        host=device["host"],
        username="sushil",
        password="sushil"
    ) as conn:
        output = conn.send_command("sh run | s router ospf")
        return output
    
with ThreadPoolExecutor() as executor:
    results = executor.map(send_cmd_to_device, DEVICES)

    for result in results:
        print(result)