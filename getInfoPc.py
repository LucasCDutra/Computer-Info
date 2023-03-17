import wmi
from classes.infoPc import InfoPc

c = wmi.WMI()
getinfo = InfoPc()

def get_adapter_config(index):
    query = f"select * from Win32_NetworkAdapterConfiguration where Index = {index}"
    return c.query(query)

def get_ethernet():
    query = 'select  * from Win32_NetworkAdapter WHERE NetConnectionID = "Ethernet"'
    for o in c.query(query):
        config = get_adapter_config(o.Index)
        for e in config:
            getinfo._macAddressEthernet = e.MacAddress
            if e.IPAddress:
                for ip in e.IPAddress:
                    getinfo._ipEthernet = ip
                    break
def get_wifi():
    query = 'select * from Win32_NetworkAdapter WHERE NetConnectionID = "WI-FI"'
    for o in c.query(query):
        config = get_adapter_config(o.Index)
        for e in config:
            getinfo._macAddressWifi = e.MacAddress
            if e.IPAddress:
                for ip in e.IPAddress:
                    getinfo._ipWifi = ip
                    break

def get_computer_information():
    query = 'SELECT UserName,Name FROM Win32_ComputerSystem'
    for o in c.query(query):
        getinfo._user = o.UserName
        getinfo._pcName = o.Name

get_wifi()
get_ethernet()
get_computer_information()
getinfo.printInfo()

input("Pressione qualquer tecla para sair.")


#Build command: pyinstaller --onefile --console --name getInfoPc -c getInfoPc.py --hidden-import wmi
