class DifferentType(object):
    def __init__(self):
        self.swaggerTypes = {
            'id': 'str', # in faked_client is int
            'name': 'str'
        }

        self.attributeMap = {
            'id': 'id',
            'name': 'name'
        }

        self.id = None
        self.name = None
