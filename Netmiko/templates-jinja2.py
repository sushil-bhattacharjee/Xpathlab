from netmiko import ConnectHandler
import ruamel.yaml as yaml
from jinja2 import Environment, FileSystemLoader
#yaml = YAML(type='safe', pure=True)
device = {
    "device_type": "cisco_ios",
    "host": "10.1.10.29",
    "username": "sushil",
    "password": "sushil",
}

def generate_config():
    
    config_data = yaml.safe_load(open("R1_router.yaml"))
    env = Environment(
        loader=FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True
        )
    template = env.get_template("ospf.j2")
    configuration = template.render(config_data)
    config_list = configuration.split('\n')
    return config_list

results = generate_config()
print(results)