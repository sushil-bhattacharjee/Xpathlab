from inv import DEVICES
from concurrent.futures import ThreadPoolExecutor
from netmiko import ConnectHandler

def send_cmd_to_device(device):
  with ConnectHandler(
    device_type="cisco_ios",
    host=device["host"],
    username="sushil",
    password="sushil"
  ) as conn:
    output = conn.send_command(command_string="sh ip int bri")
    return output
  
with ThreadPoolExecutor() as executor:
  results = executor.map(send_cmd_to_device, DEVICES)

  for result in results:
    print(result)