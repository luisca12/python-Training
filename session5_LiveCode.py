# def getFullName():
#     name = input("What is your name? ")
#     surname = input("What is your last name? ")

#     return name, surname

# output1, output2 = getFullName()

# print(f"Welcome {output1} {output2}")


# def shRun(hostname):
#     # run the show run

#####################################
# device = {
#     "device_type" : "cisco_ios",
#     "host" : "192.168.0.10",
#     "username" : "luis",
#     "password" : "cisco123",
#     "secret" : "cisco123"
# }

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

# from netmiko import ConnectHandler

# device = {
#     "device_type" : "cisco_ios",
#     "host" : "192.168.0.15",
#     "username" : "luis",
#     "password" : "cisco",
#     "secret" : "cisco",
#     'session_log': 'netmikoLog.txt',
# }

# listCommands = [
#     'interface g0/3',
#     'description Test-Interface-2',
#     'no switchport',
#     'ip add 10.30.0.1 255.255.255.0'
# ]

# shInt = "show run int g0/3"

# with ConnectHandler(**device) as sshConnection:
#     sshConnection.enable()
#     # output = sshConnection.send_command("show ip int br")
#     outpu1 = sshConnection.send_command(shInt)
#     # outpu2 = sshConnection.send_command("show int status")

#     print(f"Interface G0/1 before changes: {outpu1}")
#     sshConnection.send_config_set(listCommands)

#     outpu2 = sshConnection.send_command(shInt)
#     print(f"Interface G0/1 after changes: {outpu1}")

#####################################################
# from netmiko import ConnectHandler


# listDevices = [
#     '192.168.0.15',
#     '192.168.0.16',
#     '192.168.0.17',
# ]

# def shCommd(command):
#     device = {
#         "device_type" : "cisco_ios",
#         "host" : "192.168.0.15",
#         "username" : "luis",
#         "password" : "cisco",
#         "secret" : "cisco",
#         'session_log': 'netmikoLog.txt',
#     }

#     try:
#         with ConnectHandler(**device) as sshConnection:
#             sshConnection.enable()
#             cmmdOutput = sshConnection.send_command(command)

#             print(f"This is the output of the command: {command}\n{cmmdOutput}")

#             try:
#                 if "15.2" in cmmdOutput:
#                     print(f"Update is required")
#                 else:
#                     print(f"Update is NOT required")
#             except Exception as error:
#                 print(error)
#     except Exception as error:
#         print(error)


# shCommd("show version")

