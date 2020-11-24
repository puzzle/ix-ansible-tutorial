#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Copyright: ...
# ...

DOCUMENTATION = r'''
---
module: tutorial_module1
short_description: List VirtualBox VMs
description:
    - This module lists all VirtualBox VMs
version_added: "2.10"
options:
    state:
        description:
            - all, list all VMs
            - running, list only running VMs
        required: false
        default: all
        choices=['all', 'running']
        type: str
notes: []
requirements:
    - Installation of Virtual Box
    - VBoxManage command line tool
author: "Max Mustermann (max.muster@example.com)"
'''

EXAMPLES = r'''
- name: "List VMs"
  tutorial_module1:
  register: _all_vms
- name: "List VMs"
  tutorial_module1:
    only_running: true
  register: _all_running_vms
'''

RETURN = r'''

'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.tutorial_utils import VboxVMS


def main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(
                type='str',
                default='all',
                choices=['all', 'running'],
                required=False
            )
        )
    )

    state = module.params['state']
    vboxvm = VboxVMS(module)
    if state == 'running':
        vmlist = vboxvm.get_running()
    else:
        vmlist = vboxvm.get_all()

    result = dict(
        changed=False,
        vmlist=vmlist
    )

    module.exit_json(**result)


if __name__ == '__main__':
    main()
