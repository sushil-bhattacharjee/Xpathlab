from ncclient import manager

# Device details
device = {
    'host': 'sandbox-iosxr-1.cisco.com',
    'port': 830,
    'username': 'admin',
    'password': 'C1sco12345',
    'hostkey_verify': False,
    #'device_params': {'name': 'iosxr'},  # Use 'iosxr' for IOS XR, 'nexus' for Nexus, etc.
}

# NETCONF filter to retrieve the running configuration
netconf_filter = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-native"/>
</filter>
"""

def get_config():
    with manager.connect(**device) as m:
        # Retrieve the running configuration
        config = m.get_config(source='running', filter=netconf_filter).data_xml
        print(config)

if __name__ == "__main__":
    get_config()
