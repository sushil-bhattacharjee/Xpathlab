from scrapli_netconf import NetconfDriver

MY_DEVICE = {
    "host": "sandbox-iosxr-1.cisco.com",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
}

conn = NetconfDriver(**MY_DEVICE)
conn.open()
#myfilter = "//Loopback"
#myfilter = "//router-ospf//ospf"
#myfilter = "/native/router//network"
myfilter = """
<interfaces xmlns="http://openconfig.net/yang/interfaces">
</interface>
"""
#response = conn.get(filter_=myfilter, filter_type="xpath")
response = conn.get(filter_=myfilter, filter_type="subtree")
#response = conn.get_config(filter_=myfilter, filter_type="xpath")
print(response.result)