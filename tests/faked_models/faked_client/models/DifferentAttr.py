class DifferentAttr(object):
    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'name': 'str' # in other_faked_client is alias
        }

        self.attributeMap = {
            'id': 'id',
            'name': 'name'
        }

        self.id = None
        self.name = None
