# pycyber
apollo cyber python package

## Quick start

#### Install
You can install `pycyber` via cmd below.
```shell
pip3 install pycyber
```

#### Example
Then you can open two shell windows. One receives messages via the `listener` command, another to send a message via the `talker` command.
```shell
~$ listener

# another window
~$ talker
```

#### Usage
1. Then you can import `pycyber` in your python file.
```python
from pycyber import cyber
```

There are some examples in `pycyber/examples`.

2. Also supports some commands of cyber, such as
```
cyber_channel
cyber_launch
cyber_node
cyber_service
```
Below commands are currently not supported.
```
cyber_monitor
cyber_recorder
```

#### env
You can set cyber IP address by below command.
```shell
export CYBER_IP=127.0.0.1
```
