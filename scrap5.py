from scrapli_netconf import NetconfDriver

MY_DEVICE = {
    #"host": "10.1.10.29",
    "host": "10.1.10.51",
    "auth_username": "sushil",
    "auth_password": "sushil",
    "auth_strict_key": False,
}

conn = NetconfDriver(**MY_DEVICE)
conn.open()
#myfilter = "//interfaces-state"
#myfilter = "//interfaces-state//statistics[in-unicast-pkts > 0]"
#myfilter = "//interfaces-state//statistics[in-unicast-pkts > 0]/../name"
myfilter = """
 <interfaces xmlns="http://openconfig.net/yang/interfaces">
 </interfaces>
 """
response = conn.get(filter_=myfilter, filter_type="subtree")
print(response.result)