from netmiko import ConnectHandler


user = "kris"
password = "cisco"
device = "192.168.21.136"
community = "show run | inc snmp-server"
command = "snmp-server community KYNDRYL ro"


currentNetDevice = {
    'device_type': 'cisco_xe',
    'ip': device,
    'username': user,
    'password': password,
    'secret': password,
    'global_delay_factor': 2.0,
    'timeout': 120,
    'verbose': True
}

with ConnectHandler(**currentNetDevice) as sshAccess:
    communityOut = sshAccess.send_command(community)
    print(communityOut)
    
    if "KYNDRYL" in communityOut:
        print("The Kyndryl community is already configured")
    else:
        sshAccess.send_config_set(command)
        print("SNMP KYNDRYL community was configured successfully")
        
    
    