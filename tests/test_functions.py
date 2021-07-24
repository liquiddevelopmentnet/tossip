from tossip import Tossip

def test_collectUDIDs():
    udids = Tossip.getConnectedDeviceUDIDs()
    print(udids)

def test_validatePairing():    
    udids = Tossip.getConnectedDeviceUDIDs()
    print(Tossip.validatePairing(udids[0]))

def test_pair():
    print(Tossip.pair())

def test_unpair():
    print(Tossip.unpair())