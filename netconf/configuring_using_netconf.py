from ncclient import manager
from ncclient.xml_ import new_ele, sub_ele 
conn = manager.connect(host='192.168.255.84', port='830', username='juniper', password='Juniper', timeout=10, device_params={'name':'junos'}, hostkey_verify=False)

# lock configuration and make configuration changes conn.lock()
conn.lock()


# build configuration
config = new_ele('system')
sub_ele(config, 'host-name').text='master'
sub_ele(config, 'domain-name').text='python'

# send, validate, and commit config conn.load_configuration(config=config)


conn.load_configuration(config=config)
conn.validate()
commit_config= conn.commit()
print(commit_config.tostring)
# unlock config
conn.unlock()
#close session
conn.close_session()



