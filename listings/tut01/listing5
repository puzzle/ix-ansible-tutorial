# copyright, author, ...

DOCUMENTATION = '''
    name: tutorial_inventory
    plugin_type: inventory
    short_description: generate random hostname
    description:
        - A (useles) example inventory for our tutorial.
        - Creates inventory with random hostnames.
        - Creates group C(randomhosts).
        - Defines variables C(foo) an C(bar)
    options:
        plugin:
            description: Name of this plugin
            required: True
        num_hosts:
            description: number of random hosts
            required: True
        name_len:
            description: length of hostname (number of characters)
            type: int
            required: True
        hostname_chars:
            description: character used in random hostnames
            required: True
            type: string or list
'''

EXAMPLES = '''
    plugin: tutorial_inventory
    num_hosts: 10
    name_len: 5
    hostname_chars: abcdefghijkxyz
'''

from ansible.plugins.inventory import BaseInventoryPlugin
import random
import os


class InventoryModule(BaseInventoryPlugin):

    NAME = 'tutorial_inventory'

    def __init__(self):
        super(InventoryModule, self).__init__()

    def verify_file(self, path):
        ''' verify the inventory file '''
        return os.path.exists(path)

    def parse(self, inventory, loader, path, cache=False):
        ''' parse the inventory file '''
    
        super(InventoryModule, self).parse(inventory,
                                           loader,
                                           path,
                                           cache=cache)

        config = self._read_config_data(path)

        grp_all = inventory.groups['all']
        grp_all.set_variable('foo', 'testval1')

        inventory.add_group('randomhosts')
        grp_randomhosts = inventory.groups['randomhosts']
        grp_randomhosts.set_variable('bar', 'testval2')

        for _ in range(config['num_hosts']):
            rand_host = ''.join(
                random.choice(config['hostname_chars'])
                for _ in range(config['name_len']))
            inventory.add_host(rand_host)
            inventory.add_child('randomhosts', rand_host)
