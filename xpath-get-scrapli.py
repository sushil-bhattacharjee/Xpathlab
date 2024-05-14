from scrapli_netconf import NetconfDriver

MY_DEVICE = {
    "host": "10.1.10.29",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
}

conn = NetconfDriver(**MY_DEVICE)
conn.open()
#myfilter = "//Loopback"
#myfilter = "//router-ospf//ospf"
#myfilter = "/native/router//network"
myfilter = "//interfaces-state//statistics[out-unicast-pkts > 1000]/../name"
response = conn.get(filter_=myfilter, filter_type="xpath")
#response = conn.get_config(filter_=myfilter, filter_type="xpath")
print(response.result)