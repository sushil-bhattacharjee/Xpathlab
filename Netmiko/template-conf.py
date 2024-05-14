from netmiko import ConnectHandler
import ruamel.yaml as yaml
from jinja2 import Environment, FileSystemLoader

device = {
    "device_type": "cisco_xe",
    "host": "10.1.10.28",
    "username": "sushil",
    "password": "sushil",
}

def generate_config():
    config_data = yaml.safe_load(open("CSR1K1703.yaml"))
    env = Environment(
        loader=FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True
        )
    template = env.get_template("ospf.j2")
    configuration = template.render(config_data)
    print(configuration)
    print(type(configuration))
    config_list = configuration.split('\n')
    return config_list
   

results = generate_config()
print(results)
print(type(results))

def push_configs_to_device(config_list):
    with ConnectHandler(**device) as conn:
        output = conn.send_config_set(config_commands=config_list)
    return output

config_list = generate_config()
results2 = push_configs_to_device(config_list)
print(results2)

with ConnectHandler(**device) as conn:
    showoutput = conn.send_command("sh run | s router ospf")
print(showoutput)