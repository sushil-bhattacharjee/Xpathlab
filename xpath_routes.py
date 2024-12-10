from lxml import etree
from rich import print


xmldata = '''
<Routes>
  <route>
    <prefix>192.0.2.0</prefix>
    <length>24</length>
    <next-hop>10.100.1.2</next-hop>
    <metric>20</metric>
  </route>
  <route>
    <prefix>198.51.100.0</prefix>
    <length>24</length>
    <next-hop>192.168.31.5</next-hop>
    <metric>40</metric>
  </route>
  <route>
    <prefix>198.51.100.0</prefix>
    <length>25</length>
    <next-hop>10.100.1.2</next-hop>
    <metric>30</metric>
  </route>
  <route>
    <prefix>203.0.113.0</prefix>
    <length>24</length>
    <next-hop>172.31.11.1</next-hop>
    <metric>30</metric>
  </route>
</Routes>
'''

# Parse XML
tree = etree.fromstring(xmldata)

# Print the list of prefixes
xpath_list_of_prefix = '//prefix'
list_of_prefix = tree.xpath(xpath_list_of_prefix)

print("\n[bold cyan]List of Prefixes:[/bold cyan]")
for prefix in list_of_prefix:
    print(f"[green]{prefix.text}[/green]")

# Print the next hop for the prefix 198.51.100.0
xpath_prefix = "//route[prefix='198.51.100.0'][length='24']/next-hop"
next_hops = tree.xpath(xpath_prefix)

print("\n[bold cyan]Next hops for prefix 198.51.100.0:[/bold cyan]")
for next_hop in next_hops:
    print(f"[yellow]{next_hop.text}[/yellow]")