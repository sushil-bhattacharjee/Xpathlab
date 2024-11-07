from lxml import etree

# Sample XML data (you can also read this from a file)
xml_data = '''
<interface>
    <GigabitEthernet>
        <name>1</name>
        <description>Interface for VRF CustomerA</description>
        <vrf>
            <forwarding>CustomerA</forwarding>
        </vrf>
        <ip>
            <address>
                <primary>
                    <address>10.1.10.77</address>
                    <mask>255.255.255.0</mask>
                </primary>
            </address>
        </ip>
        <mop>
            <enabled>false</enabled>
            <sysid>false</sysid>
        </mop>
        <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
            <auto>true</auto>
        </negotiation>
    </GigabitEthernet>
    <GigabitEthernet>
        <name>2</name>
        <vrf>
            <forwarding>CustomerB</forwarding>
        </vrf>
        <ip>
            <address>
                <primary>
                    <address>10.20.20.77</address>
                    <mask>255.255.255.0</mask>
                </primary>
            </address>
        </ip>
        <mop>
            <enabled>false</enabled>
            <sysid>false</sysid>
        </mop>
        <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
            <auto>true</auto>
        </negotiation>
    </GigabitEthernet>
    <GigabitEthernet>
        <name>3</name>
        <ip>
            <address>
                <primary>
                    <address>10.20.30.1</address>
                    <mask>255.255.255.0</mask>
                </primary>
            </address>
            <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                <ospf>
                    <process-id>
                        <id>177</id>
                        <area>
                            <area-id>0</area-id>
                        </area>
                    </process-id>
                </ospf>
            </router-ospf>
        </ip>
        <ipv6>
            <address>
                <prefix-list>
                    <prefix>2001:DB8:C18:1:260:3EFF:FE47:1530/64</prefix>
                </prefix-list>
            </address>
        </ipv6>
        <mop>
            <enabled>false</enabled>
            <sysid>false</sysid>
        </mop>
        <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
            <auto>true</auto>
        </negotiation>
    </GigabitEthernet>
    <GigabitEthernet>
        <name>4</name>
        <description>Configured by Yangsuite</description>
        <mpls>
            <ip xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mpls"/>
        </mpls>
        <ip>
            <address>
                <primary>
                    <address>10.10.1.1</address>
                    <mask>255.255.255.0</mask>
                </primary>
            </address>
        </ip>
        <ipv6>
            <address>
                <prefix-list>
                    <prefix>2001:DB8:C18:2:260:3EFF:FE47:1530/64</prefix>
                </prefix-list>
            </address>
        </ipv6>
        <mop>
            <enabled>false</enabled>
            <sysid>false</sysid>
        </mop>
        <cdp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-cdp">
            <enable>true</enable>
        </cdp>
        <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
            <auto>true</auto>
        </negotiation>
    </GigabitEthernet>
    <Loopback>
        <name>0</name>
        <description>Interface Loopback0 for router-identity</description>
        <ip>
            <address>
                <primary>
                    <address>7.7.7.7</address>
                    <mask>255.255.255.255</mask>
                </primary>
            </address>
        </ip>
    </Loopback>
    <Loopback>
        <name>100</name>
        <description>Interface Loopback100 for CustomerA-identity</description>
        <ip>
            <address>
                <primary>
                    <address>100.7.7.7</address>
                    <mask>255.255.255.0</mask>
                </primary>
            </address>
        </ip>
    </Loopback>
    <Loopback>
        <name>200</name>
        <description>Created by NSO Service Template</description>
        <ip>
            <address>
                <primary>
                    <address>200.200.200.200</address>
                    <mask>255.255.255.255</mask>
                </primary>
            </address>
        </ip>
    </Loopback>
</interface>
'''
xml_data_2 = '''
<protocols>
    <ospf>
        <area>
            <name>0.0.0.0</name>
            <interface>
                <name>ge-0/0/0.0</name>
                <interface-type>p2p</interface-type>
            </interface>
        </area>
    </ospf>
    <ospf3>
        <area>
            <name>0.0.0.1</name>
            <interface>
                <name>xe-0/0/1.0</name>
                <hello-interval>1</hello-interval>
                <dead-interval>4</dead-interval>
            </interface>
        </area>
    </ospf3>
</protocols>
'''
# Parse the XML data
tree = etree.fromstring(xml_data_2)
xpath_filter = '(//*/ipv6/address//prefix)[2]'
xpath_filter_2 = '//*/ipv6'
xpath_filter_LB2 = '//Loopback[2]//primary/address'
xpath_filter_child = '//Loopback[2]//*[self::address]'
xpath_filter_3 = '//interface/*[self::interface-type]'
# Define the namespaces
# namespaces = {
#     'base': 'urn:ietf:params:xml:ns:netconf:base:1.0',
#     'native': 'http://cisco.com/ns/yang/Cisco-IOS-XE-native'
# }

# Find all IPv6 addresses
# Find all IPv6 addresses
results = tree.xpath(xpath_filter_3)
print(results)
# Print the filtered result
for result in results:
    print(result.text)
