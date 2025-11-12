# from netmiko import ConnectHandler

# sshConnection = ConnectHandler(
#     device_type="cisco_ios",
#     host="192.168.0.15",
#     username="luis",
#     password="cisco",
#     secret="cisco"
# )
# sshConnection.enable()
# sshConnection.disconnect()

#####################################################
# from netmiko import ConnectHandler

# device = {
#     "device_type" : "cisco_ios",
#     "host" : "192.168.0.15",
# 	"username" : "luis",	
# 	"password" : "cisco",
# 	"secret" : "cisco"
# }

# sshConnection = ConnectHandler(**device)
# sshConnection.enable()
# sshConnection.disconnect()

#####################################################
# from netmiko import ConnectHandler

# device = {
#     "device_type" : "cisco_ios",
#     "host" : "192.168.0.15",
# 	"username" : "luis",	
# 	"password" : "cisco",
# 	"secret" : "cisco"
# }

# with ConnectHandler(**device) as sshConnection:
# 	sshConnection.enable()

#####################################################
# from netmiko import ConnectHandler

# device = {
#     "device_type" : "cisco_ios",
#     "host" : "192.168.0.15",
# 	"username" : "luis",	
# 	"password" : "cisco",
# 	"secret" : "cisco"
# }

# with ConnectHandler(**device) as sshConnection:
#     sshConnection.enable()
#     sshConnection.send_command("show version")

#####################################################
# from netmiko import ConnectHandler

# device = {
#     "device_type" : "cisco_ios",
#     "host" : "192.168.0.15",
# 	"username" : "luis",	
# 	"password" : "cisco",
# 	"secret" : "cisco"
# }

# listCmmnds = [
#     'interface g0/0',
#     'description Test-Int'
# ]

# with ConnectHandler(**device) as sshConnection:
#     sshConnection.enable()
#     sshConnection.send_config_set(listCmmnds)

#####################################################
# from netmiko import ConnectHandler

# device = {
#     "device_type" : "cisco_ios",
#     "host" : "192.168.0.15",
# 	"username" : "luis",	
# 	"password" : "cisco",
# 	"secret" : "cisco"
# }

# cmnds = [
#     'interface g0/0',
#     'description Test-Int'
# ]

# shVersion = "show version"

# with ConnectHandler(**device) as sshConnection:
# 	sshConnection.enable()
# 	output = sshConnection.send_command(shVersion)

# 	if "15.2" in output:
# 		print("Update is needed")
# 		sshConnection.send_config_set(cmnds)
# 	else:
# 		print("Device version in compliance")
	
#####################################################
#                   Practice                        #
#####################################################
# from netmiko import ConnectHandler

# device = {
#     "device_type" : "cisco_ios",
#     "host" : "192.168.0.15",
# 	"username" : "luis",	
# 	"password" : "cisco",
# 	"secret" : "cisco"
# }

# cmnds = [
#     'interface g0/0',
#     'description Test-Int'
# ]

# shVersion = "show version"

# try:
#     with ConnectHandler(**device) as sshConnection:
#         sshConnection.enable()
#         output = sshConnection.send_command(shVersion)

#         if "15.2" in output:
#             print("Update is needed")
#             sshConnection.send_config_set(cmnds)
#         else:
#             print("Device version in compliance")
# except Exception as error:
#     print(error)