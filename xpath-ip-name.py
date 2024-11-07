from scrapli_netconf import NetconfDriver

MY_DEVICE = {
    "host": "10.1.10.77",
    #"host": "10.1.10.28",
    "auth_username": "sushil",
    "auth_password": "sushil",
    "auth_strict_key": False,
}

conn = NetconfDriver(**MY_DEVICE)
conn.open()


#Show the running config
print("Show running config\n")
run_config = "//native"
response = conn.get_config(filter_=run_config, filter_type="xpath")
#print(response.result)

#Show the hostname
print("Show the hostname\n")
host_name = "//native/hostname"
response = conn.get_config(filter_=host_name, filter_type="xpath")
print(response.result)

#Show the CPU load
print("Show the CPU load\n")
cpu_load = "//monitor[child::load]"
response = conn.get_config(filter_=cpu_load, filter_type="xpath")
print(response.result)

#Find the username which has privilage level=15
user_name_prv15 = "//username[privilege=15]/name"

#Show the ip address for the interface name "GigabitEthernet2"
print("Show the ip address for the interface name GigabitEthernet2\n")
Gi2_ip = "//GigabitEthernet[name=2]//primary/*"
response = conn.get_config(filter_=Gi2_ip, filter_type="xpath")
print(response.result)

#Show the second element node of GigabitEthernet
print("Show the ip address of GigabitEthernet2\n")
Gi2 = "//GigabitEthernet[2]/*" #Show the ip address of GigabitEthernet2
response = conn.get_config(filter_=Gi2, filter_type="xpath")
print(response.result)

#Show the element node which has child name "address"
print("Show all the ip address of the device\n")
sh_ip_int = "//primary[child::address]" #Show all the ip address of the device
response = conn.get_config(filter_=sh_ip_int, filter_type="xpath")
print(response.result)

#Show the element node name Loopback, which is second
print("Show the ip address of 2nd Loopback\n")
LB_ip = "//Loopback[2]/*" #Show the ip address of 2nd Loopback
response = conn.get_config(filter_=LB_ip, filter_type="xpath")
print(response.result)

#Show the name of second Loopback interface 
print("Show the name of second Loopback interface\n")
LB_name = "//Loopback[2]/name"
response = conn.get_config(filter_=LB_name, filter_type="xpath")
print(response.result)

#Show the interface which has in-unicast>0
print("Show the interfaces name which have in-unicast-pkts>0\n")
active_interface = "/interfaces-state//statistics[in-unicast-pkts > 0 ]/../name"
response = conn.get(filter_=active_interface, filter_type="xpath")
print(response.result)

#In the myfliter fill the above filter name
myfilter = user_name_prv15

response = conn.get_config(filter_=myfilter, filter_type="xpath")
print(response.result)