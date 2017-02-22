#pylint: skip-file
class BandwidthInfo(object):
    def __init__(self):
        self.swaggerTypes = {
            'serviceClass': 'str',
            'dscp': 'str',
            'bandwidthPercent': 'int'
        }

        self.attributeMap = {
            'serviceClass': 'class',
            'dscp': 'dscp',
            'bandwidthPercent': 'bandwidthPercent'
        }

        self.serviceClass = None # str
        self.dscp = None  # str
        self.bandwidthPercent = None  # int
