from lxml import etree
from rich import print

xml_data = '''
<Interfaces>
  <Loopback>
    <name>0</name>
    <ip>
      <address>
        <primary>
          <address>10.1.1.17</address>
          <mask>255.255.255.255</mask>
        </primary>
      </address>
    </ip>
  </Loopback>
  <GigabitEthernet>
    <name>0/1</name>
    <ip>
      <address>
        <primary>
          <address>10.1.2.1</address>
          <mask>255.255.255.252</mask>
        </primary>
      </address>
    </ip>
  </GigabitEthernet>
  <GigabitEthernet>
    <name>0/2</name>
    <ip>
      <address>
        <primary>
          <address>10.1.2.5</address>
          <mask>255.255.255.252</mask>
        </primary>
      </address>
    </ip>
  </GigabitEthernet>
</Interfaces>
'''

tree = etree.fromstring(xml_data)

# Correct XPath to find 'address' nodes
xpath_filter_ipv4 = '/*//ip/address/primary/address'
xpath_filter1 = '//primary/address'
output = tree.xpath(xpath_filter_ipv4)
output1 = tree.xpath(xpath_filter1)

# Print the extracted IP addresses
print("[#FFC0CB] All IPv4 address")
for result in output:
    print(f"[bold green]IP Address:[bold blue] {result.text}")

    
# Print the IP address of GigabitEthernet only
GE_xpath = '//GigabitEthernet//primary/address'
GE_ipv4 = tree.xpath(GE_xpath)
print("\n[#FFA500]Gigabit Ethernet IPv4 address")
for result_GE in GE_ipv4:
    print(f"[bold purple]GigabitEthernet IP address:[bold red]{result_GE.text}")

# print("[#FFC0CB]This is pink[/#FFC0CB]")
# print("[#FFA500]This is orange[/#FFA500]")

# Print the IP address of first line card
firstlinecard = "//GigabitEthernet[name[starts-with(text(), '0')]]//primary/address"
ip_0 = tree.xpath(firstlinecard)
print("\n[#FFA500]First line card GigabitEthernet0/x IPv4 address")
for ipv4_GE0 in ip_0:
    print(f"[bold white]GigabitEthernet0/x IP address:[bold yellow]{ipv4_GE0.text}")
    
    
# Print the second GigabitEthernet IP address
Scnd_ipv4_GE0 = '//GigabitEthernet[position()=2]//primary/address'
linecard_GE0 = '//GigabitEthernet[1]//primary/address' #Optimized to above xpath
ipv4_2 = tree.xpath(Scnd_ipv4_GE0)
print("\n[#FFA500]Second GigabitEthernet IPv4 address")
for result_ipv4_2 in ipv4_2:
    print(f"[bold white]GigabitEthernet0/1 IP address:[bold yellow]{result_ipv4_2.text}")