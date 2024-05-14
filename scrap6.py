from scrapli_netconf import NetconfDriver
from lxml import etree
from io import StringIO

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
conn.close()
et = etree.parse(StringIO(response.result), parser=etree.HTMLParser(recover=True))
#print(response.result)
root = et.getroot()
#print(root)
path = root.xpath("//subinterface/ipv4//ip")
#print(path)
for element in path:
    print(element.text)
    interface = element.xpath("ancestor::interface/name/text()")[0]
    print(interface)
    for children in element:
        print(f"     {children.text}")
        print("\n")