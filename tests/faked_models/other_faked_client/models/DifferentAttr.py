class DifferentAttr(object):
    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'alias': 'str' # in faked_client is name
        }

        self.attributeMap = {
            'id': 'id',
            'alias': 'name'
        }

        self.id = None
        self.alias = None
