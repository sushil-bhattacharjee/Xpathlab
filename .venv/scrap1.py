from scrapli_netconf import NetconfDriver

MY_DEVICE = {
    "host" : "10.1.10.29",
    "auth_username": "sushil",
    "auth_password": "cisco",
    "auth_strict_key": False,
}

conn = NetconfDriver(**MY_DEVICE)
conn.open()
myfilter = "/native"
response = conn.get(filter_=myfilter, filter_type="xpath")
print(response.result)