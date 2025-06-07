from ncclient import manager
from ncclient.xml_ import new_ele, sub_ele

# make a connection object
def connect(host, port, user, password):
    connection = manager.connect(host=host, port=port, username=user, password=password, timeout=10, device_params={'name':'junos'}, hostkey_verify=False)
    return connection

# execute show commands
def show_cmds(conn, cmd):
    result = conn.command(cmd, format='text')
    return result

# push out configuration
def config_cmds(conn, config):
    conn.lock()
    conn.load_configuration(config=config)
    commit_config = conn.commit()
    conn.unlock()
    return commit_config.tostring

if __name__ == '__main__':
    conn = connect('192.168.255.84','830','juniper','Juniper')
    result = show_cmds(conn, 'show version')
    print('show version: ' + str(result))
    new_config = new_ele('system')
    sub_ele(new_config, 'host-name').text = 'jx1'
    sub_ele(new_config, 'domain-name').text = 'jx1.local'
    result = config_cmds(conn, new_config)
    print('change id: ' + str(result))
    conn.close_session()
    
    
    
    





