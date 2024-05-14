from scrapli_netconf import NetconfDriver
from lxml import etree
from io import StringIO


MY_DEVICE = {
    "host": "sandbox-iosxr-1.cisco.com",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
}

conn = NetconfDriver(**MY_DEVICE)
conn.open()

myfilter = """
<interfaces xmlns="http://openconfig.net/yang/interfaces">
</interface>
"""

response = conn.get(filter_=myfilter, filter_type="subtree")
conn.close()

et = etree.parse(StringIO(response.result), parser=etree.HTMLParser(recover=True))
root = et.getroot()

path = root.xpath("//subinterface/ipv4//config")
for element in path:
    print(element.text)
    interface = element.xpath("ancestor::interface/name/text()")[0]
    print(interface)
    for children in element:
        print(f"    {children.text}")

