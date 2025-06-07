#!/usr/bin/env python3
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import sys

dev = Device(host='192.168.255.84', user='juniper', passwd='Juniper')

try:
    dev.open()
except Exception as err:
    print(err)
    sys.exit(1)

config_change = """
 <system>
    <host-name>master</host-name>
    <domain-name>python</domain-name>
 </system>
"""

cu = Config(dev)
cu.lock()
cu.load(config_change)
cu.commit()
cu.unlock()

dev.close()