from lxml import etree

# Sample XML data (you can also read this from a file)
xml_data = '''
<data>
  <native>
    <ip>
      <pim>
        <send-rp-discovery/>
      </pim>
      <routing-new>
        <routing>
          <protocol>
            <purge/>
          </protocol>
        </routing>
      </routing-new>
    </ip>
    <interface>
      <GigabitEthernet>
        <name>1</name>
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
        <logging>
          <event>
            <link-status/>
          </event>
        </logging>
        <mop>
          <enabled>false</enabled>
          <sysid>false</sysid>
        </mop>
        <negotiation>
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
        <logging>
          <event>
            <link-status/>
          </event>
        </logging>
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
        </ip>
        <ipv6>
          <address>
            <prefix-list>
              <prefix>2001:DB8:C18:1:260:3EFF:FE47:1530/64</prefix>
            </prefix-list>
          </address>
        </ipv6>
        <logging>
          <event>
            <link-status/>
          </event>
        </logging>
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
        <logging>
          <event>
            <link-status/>
          </event>
        </logging>
        <mop>
          <enabled>false</enabled>
          <sysid>false</sysid>
        </mop>
        <cdp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-cdp">
          <enable>true</enable>
          <tlv>
            <app/>
            <server-location/>
            <location/>
          </tlv>
        </cdp>
        <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
          <auto>true</auto>
        </negotiation>
      </GigabitEthernet>
      <Loopback>
        <name>0</name>
        <ip>
          <address>
            <primary>
              <address>7.7.7.7</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
        <logging>
          <event>
            <link-status/>
          </event>
        </logging>
      </Loopback>
      <Loopback>
        <name>100</name>
        <ip>
          <address>
            <primary>
              <address>100.7.7.7</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
        <logging>
          <event>
            <link-status/>
          </event>
        </logging>
      </Loopback>
    </interface>
    <track>
      <timer/>
    </track>
    <vtp/>
    <network-clock>
      <input-source/>
    </network-clock>
    <l2vpn>
      <evpn_cont>
        <evpn>
          <router-id/>
        </evpn>
      </evpn_cont>
    </l2vpn>
    <mpls>
      <ldp>
        <enable2>
          <router-id/>
        </enable2>
      </ldp>
    </mpls>
    <router>
      <bgp>
        <id>65077</id>
        <neighbor>
          <id>10.12.12.12</id>
          <update-source>
            <interface>
              <Loopback>0</Loopback>
            </interface>
          </update-source>
        </neighbor>
        <address-family>
          <with-vrf>
            <ipv4>
              <af-name>unicast</af-name>
              <vrf>
                <name>CustomerA</name>
                <ipv4-unicast>
                  <neighbor>
                    <id>10.1.10.28</id>
                    <update-source>
                      <interface>
                        <Loopback>0</Loopback>
                      </interface>
                    </update-source>
                  </neighbor>
                </ipv4-unicast>
              </vrf>
              <vrf>
                <name>CustomerB</name>
                <ipv4-unicast>
                  <neighbor>
                    <id>10.1.10.30</id>
                    <update-source>
                      <interface>
                        <Loopback>0</Loopback>
                      </interface>
                    </update-source>
                  </neighbor>
                </ipv4-unicast>
              </vrf>
            </ipv4>
          </with-vrf>
        </address-family>
      </bgp>
    </router>
  </native>
</data>

'''

# Parse the XML data
tree = etree.fromstring(xml_data)

#Find all ipv4 address
all_ipv4 = '//native/interface/*/ip/address/primary/address'
all_ipv4_sh = '//*/ip//primary/address'

#Find all ipv6 address
all_ipv6 = '//native/interface/*/ipv6/address/prefix-list/prefix'
all_ipv6_sh = '//*/ipv6//prefix'

#Find all Loopback addresses
lb = '//native/interface/Loopback/ip/address/primary/address'
lb_sh = '//Loopback/ip//primary/address'
lb_100 = '//Loopback[name=100]/ip//primary/address'

#Find 2nd ipv6 address
xpath_filter = '(//GigabitEthernet/ipv6/address/prefix-list/prefix)[2]'

#Find 2nd Loopback address
lb2 = '(//native/interface/Loopback/ip/address/primary/address)[2]'
lb2_sh = '(//Loopback/ip//primary/address)[2]'

# Define the namespaces
# namespaces = {
#     'base': 'urn:ietf:params:xml:ns:netconf:base:1.0',
#     'native': 'http://cisco.com/ns/yang/Cisco-IOS-XE-native'
# }

# Find all IPv6 addresses
# Find all IPv6 addresses
output = tree.xpath(lb_100)
print(output)
# Print the IPv6 addresses
for result in output:
    print(result.text)
