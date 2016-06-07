class DifferentType(object):
    def __init__(self):
        self.swaggerTypes = {
            'id': 'int', # in other_faked_client is str
            'name': 'str'
        }

        self.attributeMap = {
            'id': 'id',
            'name': 'name'
        }

        self.id = None
        self.name = None
