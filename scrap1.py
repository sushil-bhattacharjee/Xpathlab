from scrapli_netconf import NetconfDriver

MY_DEVICE = {
    #"host": "10.1.10.29",
    "host": "10.1.10.28",
    "auth_username": "sushil",
    "auth_password": "sushil",
    "auth_strict_key": False,
}

conn = NetconfDriver(**MY_DEVICE)
conn.open()
myfilter = "/native/interface/Loopback/ip/address"
response = conn.get_config(filter_=myfilter, filter_type="xpath")
print(response.result)