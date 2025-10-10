# green = 1
# x = [
#     "red", 
#     "2011",
#     "Ford',
#     green
# ]

# green = True
# x1 = [
#     'red', 
#     2011 
#     'Ford",
#     green
# ]

# green = "green"
# x2 = [
#     "red", 
#     "2011", 
#     "Ford",
#     green
# ]

#################################################

# green = 1
# z = { 
#     "color": 'green'
#     "brand": "Honda", 
# }

# green = True
# z1 = { 
#     'color': green, 
#     "brand": "Honda", 
# }

# green = "green" 
# z2 = { 
#     'color': green 
#     "brand": "Honda", 
# }

#################################################

# showRunTXT = """
#     Router# show running-config
# Building configuration...

# Current configuration : 6208 bytes
# !
# version 17.6
# service timestamps debug datetime msec
# service timestamps log datetime msec
# service password-encryption
# !
# hostname R1-LAB
# !
# boot-start-marker
# boot-end-marker
# !
# logging buffered 51200 warnings
# no aaa new-model
# clock timezone CST -6 0
# !
# ip cef
# no ipv6 cef
# !
# snmp-server community private RO
# snmp-server location LAB-ROUTER-01
# !
# interface GigabitEthernet0/0
#  description *** Connection to ISP ***
#  ip address 200.1.1.2 255.255.255.252
#  ip nat outside
#  no shut
# !
# interface GigabitEthernet0/1
#  description *** LAN Segment ***
#  ip address 192.168.10.1 255.255.255.0
#  ip nat inside
#  no shut
# !
# interface GigabitEthernet0/2
#  description *** DMZ Segment ***
#  ip address 10.10.10.1 255.255.255.0
#  no shut
# !
# interface Loopback0
#  ip address 1.1.1.1 255.255.255.255
# !
# router ospf 10
#  router-id 1.1.1.1
#  network 192.168.10.0 0.0.0.255 area 0
#  network 10.10.10.0 0.0.0.255 area 0
#  passive-interface default
#  no passive-interface GigabitEthernet0/0
# !
# router bgp 65001
#  bgp log-neighbor-changes
#  neighbor 200.1.1.1 remote-as 65000
#  neighbor 200.1.1.1 description *** ISP EDGE ***
#  neighbor 200.1.1.1 update-source GigabitEthernet0/0
# !
#  address-family ipv4
#   network 192.168.10.0 mask 255.255.255.0
#   network 10.10.10.0 mask 255.255.255.0
#   neighbor 200.1.1.1 activate
#  exit-address-family
# !
# ip route 0.0.0.0 0.0.0.0 200.1.1.1
# !
# ip nat inside source list NAT_ACL interface GigabitEthernet0/0 overload
# access-list 1 permit 192.168.10.0 0.0.0.255
# access-list 1 permit 10.10.10.0 0.0.0.255
# !
# banner motd ^C
# *********************************************
# *   Unauthorized access to this device is   *
# *   strictly prohibited and will be logged  *
# *********************************************
# ^C
# !
# line con 0
#  logging synchronous
#  exec-timeout 15 0
#  privilege level 15
# line vty 0 4
#  transport input ssh
#  login local
# line vty 5 15
#  transport input ssh
#  login local
# !
# username admin privilege 15 secret 9 $9$N9JF9fj3Fi39nfj3f93nf39
# username netops privilege 15 password 0 labpass
# !
# ip ssh version 2
# crypto key generate rsa modulus 2048
# !
# ntp server 132.163.97.1 prefer
# !
# end
# Router#
# """

# community = ""

# if "private" in showRunTXT:
#     print("There is a private SNMP Community")
#     community = "private"

#     if "RO" in showRunTXT:
#         print("It's a Read Only SNMP Community")
#         community = community + "-RO"

# elif "public" in showRunTXT:
#     print("There is a public SNMP Community")
#     community = "public"

# else:
#     print("Nothing was found")

# print("The community is:", community)