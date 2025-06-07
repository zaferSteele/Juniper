from jnpr.junos import Device 
import xml.etree.ElementTree as ET
import pprint
import sys

dev = Device(host='192.168.255.84', user='juniper', passwd='Juniper')

try:
    dev.open()
except Exception as err:
    print(err)
    sys.exit(1)

result = dev.rpc.get_interface_information(interface_name='em1', terse=True)
pprint.pprint(ET.tostring(result))

# result = dev.display_xml_rpc('show interfaces em1', format='text')
print(result)

dev.close()
    