class InfoPc:
    def __init__(self,pcName = None,user = None,macAddressEthernet = None,macAddressWifi = None,ipEthernet= None,ipWifi= None):
        self._pcName =pcName
        self._user = user
        self._macAddressEthernet = macAddressEthernet
        self._macAddressWifi = macAddressWifi
        self._ipEthernet = ipEthernet
        self._ipWifi = ipWifi

        @property
        def pcName(self):
            return self._pcName

        @pcName.setter
        def nome(self, pcName):
            self._pcName = pcName

        #-=-=-=-=-=-=-=-
        @property
        def user(self):
            return self._user

        @pcName.setter
        def nome(self, user):
            self._user = user

        #-=-=-=-=-=-=-=-
        @property
        def macAddressEthernet(self):
            return self._macAddressEthernet

        @pcName.setter
        def nome(self, macAddressEthernet):
            self._macAddressEthernet = macAddressEthernet

        #-=-=-=-=-=-=-=-
        @property
        def macAddressWifi(self):
            return self._macAddressWifi

        @macAddressWifi.setter
        def nome(self, macAddressWifi):
            self._macAddressWifi = macAddressWifi

        #-=-=-=-=-=-=-=-
        @property
        def ipEthernet(self):
            return self._ipEthernet

        @ipEthernet.setter
        def nome(self, ipEthernet):
            self._ipEthernet = ipEthernet

        #-=-=-=-=-=-=-=-
        @property
        def ipWifi(self):
            return self._ipWifi

        @ipWifi.setter
        def nome(self, ipWifi):
            self._ipWifi = ipWifi


    def printInfo(self):
        print('====================================')
        print('========== ',self._pcName,' ===========')
        print('\n ')

        print('computer ------------ ',self._pcName)
        print('user ---------------- ',self._user)
        print('macAddress Wifi ----- ',self._macAddressWifi)
        print('ip Wifi ------------- ',self._ipWifi)
        print('macAddress Ethernet - ',self._macAddressEthernet)
        print('ip Ethernet --------- ',self._ipEthernet)
        print('\n ')
        print('====================================')