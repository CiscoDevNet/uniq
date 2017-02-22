#pylint: skip-file
class IWanQosInterfaceBandwidthInfo(object):
    def __init__(self):
        self.swaggerTypes = {
            'interfaceId': 'str',
            'bandwidthAllocations': 'list[BandwidthInfo]',
        }

        self.attributeMap = {
            'interfaceId': 'interfaceId',
            'bandwidthAllocations': 'bandwidthAllocations',
        }

        self.interfaceId = None # str
        self.bandwidthAllocations = None # list[BandwidthInfo]
