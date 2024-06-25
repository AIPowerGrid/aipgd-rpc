import json
from aipgrpc import Aipowergrid

aipg = Aipowergrid('aipg', 'AIPG_pass01')
blockchaininfo = aipg.getblockchaininfo()
print(json.dumps(blockchaininfo, indent=4))
print("\nThis was a successful test of the AIPG Python RPC Daemon Bridge")
