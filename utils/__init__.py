""" Package of Uniq utilities.

Including:
    utils.wait.
"""



from .wait import Wait

class Utils(object):
    pass

utils = Utils()
utils.wait = Wait()