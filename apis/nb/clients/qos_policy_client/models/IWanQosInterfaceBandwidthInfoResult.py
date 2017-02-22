#pylint: skip-file
class IWanQosInterfaceBandwidthInfoResult(object):
    def __init__(self):
        self.swaggerTypes = {
            'version': 'str',
            'response': 'IWanQosInterfaceBandwidthInfo'
        }

        self.attributeMap = {
            'version': 'version',
            'response': 'response'
        }

        self.version = None # str
        self.response = None # IWanQosInterfaceBandwidthInfo