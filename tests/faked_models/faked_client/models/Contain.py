class Contain(object):
    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'name': 'str',
            'contain': 'str'
        }

        self.attributeMap = {
            'id': 'id',
            'name': 'name',
            'contain': 'contain'
        }

        self.id = None
        self.name = None
        self.contain = None