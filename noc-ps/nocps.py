try:
    from xmlrpclib import ServerProxy, Error
except ImportError:
    from xmlrpc.client import ServerProxy, Error

class NocPS:
    """
    Inits connection with the nocps and sends data back
    Uses xmlrpc to retrieve data
    """

    def __init__(self, server, user, password, proto="http"):
        self.server = ServerProxy("{proto}://{user}:{pwd}@{srv}/xmlrpc.php".format(
            proto=proto, user=user, pwd=password, srv=server))



    def __getattr__(self, name, *args):
        def function(*args):
            """
            universal method, it forwards requested method directly to xmlrpc with all args
            """
            return getattr(self.server.PXE_API, name)(*args)

        return function
