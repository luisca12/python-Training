
########################################################While Ping Script##########################################################

# import socket
# import time

# host = 'google.com'
# port = 443
# ping_count = 0
# max_pings = 5

# while ping_count < max_pings:
#     try:
#         s = socket.socket()
#         s.settimeout(2)
#         s.connect((host, port))
#         print(f"Ping {ping_count + 1}: Success!")
#         s.close()
#     except socket.error:
#         print(f"Ping {ping_count + 1}: Failed.")
#     ping_count += 1
#     time.sleep(1)


#######################################################ACL With def##########################################################


# import getpass
# from netmiko import ConnectHandler

# aclShow = "show ip access-lists"
# aclCommand = "access-list 100 permit udp host 10.10.10.1 20.20.20.0 0.0.0.255 eq 123"

# def requestLogin():
# 	try:
# 		device = input("Please enter the device IP address: ")	
# 		username = input("Please enter your username: ")
# 		password = getpass.getpass("Please enter your password: ")

		
# 		netDevice = {
# 				'device_type': 'cisco_xe',
# 				'ip': device,
# 				'username': username,
# 				'password': password,
# 				'secret': password,
# 				'timeout': 120,
# 				'verbose': True
   				
# 			}
# 		return netDevice
# 	except Exception as e:
# 		print(f"An error occurred: {e}")



# with ConnectHandler(**requestLogin()) as sshAccess:
#     aclShowOut = sshAccess.send_command(aclShow)
#     print(aclShowOut)

#     if "permit udp host 10.10.10.1 20.20.20.0 0.0.0.255 eq ntp" in aclShowOut:
#         print("The ACL is arleady configured")
#     else:
#         sshAccess.send_config_set(aclCommand)
#         print("ACL configured successfully")
#         print(sshAccess.send_command(aclShow))




######################################################Option with List of Devices##########################################################	


# import getpass
# from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException

# aclShow = "show ip access-lists"
# aclCommand = "access-list 100 permit udp host 10.10.10.1 20.20.20.0 0.0.0.255 eq 123"

# def requestLogin():
#     username = input("Please enter your username: ")
#     password = getpass.getpass("Please enter your password: ")
#     return username, password


# def createDeviceDict(ip, username, password):
#     return {
#         'device_type': 'cisco_xe',
#         'ip': ip,
#         'username': username,
#         'password': password,
#         'secret': password,
#     }


# def main():
#     devices = ["192.168.21.136", "192.168.21.137", "10.10.10.1"]

#     username, password = requestLogin()

#     for ip in devices:
#         print(f"Connecting to {ip}...")

#         device_params = createDeviceDict(ip, username, password)

#         try:
#             with ConnectHandler(**device_params) as sshAccess:
#                 aclShowOut = sshAccess.send_command(aclShow)
#                 print(f"Output from {ip}:\n{aclShowOut}\n")
                
#                 if "permit udp host 10.10.10.1 20.20.20.0 0.0.0.255 eq ntp" in aclShowOut:
#                     print("The ACL is arleady configured")
#                 else:
#                     sshAccess.send_config_set(aclCommand)
#                     print("ACL configured successfully")
#                     print(sshAccess.send_command(aclShow))

        # except NetMikoTimeoutException:
        #     print(f"Timeout while connecting to {ip}")
        # except NetMikoAuthenticationException:
        #     print(f"Authentication failed for {ip}")
        # except Exception as e:
        #     print(f"Unexpected error with {ip}: {e}")

# main()



#######################################################Option with txt file##########################################################


# import getpass
# from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException

# aclShow = "show ip access-lists"
# aclCommand = "access-list 100 permit udp host 10.10.10.1 20.20.20.0 0.0.0.255 eq 123"

# def requestLogin():
#     username = input("Please enter your username: ")
#     password = getpass.getpass("Please enter your password: ")
#     return username, password


# def createDeviceDict(ip, username, password):
#     return {
#         'device_type': 'cisco_xe',
#         'ip': ip,
#         'username': username,
#         'password': password,
#         'secret': password,
#     }


# def main():
#     with open("devices.txt") as f:
#         devices = [line.strip() for line in f if line.strip()]


#     username, password = requestLogin()

#     for ip in devices:
#         print(f"Connecting to {ip}...")

#         device_params = createDeviceDict(ip, username, password)

#         try:
#             with ConnectHandler(**device_params) as sshAccess:
#                 aclShowOut = sshAccess.send_command(aclShow)
#                 print(f"Output from {ip}:\n{aclShowOut}\n")
                
#                 if "permit udp host 10.10.10.1 20.20.20.0 0.0.0.255 eq ntp" in aclShowOut:
#                     print("The ACL is arleady configured")
#                 else:
#                     sshAccess.send_config_set(aclCommand)
#                     print("ACL configured successfully")
#                     wrOut = sshAccess.send_config_set("do wr")
#                     print("Config saved successfully")
#                     print(wrOut)

#         except NetMikoTimeoutException:
#             print(f"Timeout while connecting to {ip}")
#         except NetMikoAuthenticationException:
#             print(f"Authentication failed for {ip}")
#         except Exception as e:
#             print(f"Unexpected error with {ip}: {e}")

# main()