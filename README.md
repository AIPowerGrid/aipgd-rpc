# AIPowerGridRPC

Crazy simple AI Power Grid RPC library, designed to work with all versions of AI Power Grid.

*"I have seen many libraries, this one... is pretty average" - Joe*

INSTALL:

```
pip install aipgrpc
```

## Setting Up Ravend (Linux)

go to your `.aipg` folder, add a `aipg.conf` file if there is not one already, in that file add:

```
rpcuser=username
rpcpassword=password
```

**Make sure you use a secure username and password!**

Then run `./aipgd` in the directory that it is located!

Examples:

```python
from aipgrpc import Aipowergrid

aipg = Aipowergrid('username', 'password')
aipg.getinfo()
aipg.listreceivedbyaddress(0, True)
```

Any other rpc method:

```python
aipg.<METHOD>(<param1>, <param2>, ...)
```

**Note**: If the username and password are incorrect, then a empty string will be returned. 

Please report any bugs by filling out an issue!

## Use it with other cryptos too!!

Just set the port when accessing:

```python
btc = Aipowergrid('username', 'password', port=8332)
```

And if you want to use a different host:

```python
btc = Aipowergrid('username', 'password', host='host.com', port=8333)
```
