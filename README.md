# noc-ps
API for NOC-PS provisioning system

It requires xmlrpclib to be installed (xmlrpc.client for Python 3)

Simple usage:
```python
from nocps import NocPS

NOCPS = NocPS(server="noc-ps.server.com", user="admin", password="password")
print(NOCPS.getPools())
```

For documentation, how to use API, and available methods, please reffer to https://www.noc-ps.com/downloads/PXE_API.html
