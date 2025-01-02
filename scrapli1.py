from scrapli_netconf.driver import NetconfDriver

my_device = {
    "host": "sandbox-iosxr-1.cisco.com",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
    "port": 830
}

filter_ = """
<components xmlns="http://openconfig.net/yang/platform">
    <component>
        <state>
        </state>
    </component>
</components>"""

conn = NetconfDriver(**my_device)
conn.open()
response = conn.get(filter_=filter_, filter_type="subtree")
print(response.result)