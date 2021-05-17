#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Copyright: ...
# ...

DOCUMENTATION = r'''
---
module: tutorial_module_2
short_description: Start or stop VM
description:
    - This module starts or stops VirtualBox VMs
version_added: "2.10"
options:
    name:
        description:
          - name of VM
    state:
        description:
          - started
          - stopped
        required: true
        default: all
        choices=['running', 'poweroff']
        type: str
notes: []
requirements:
    - Installation of Virtual Box
    - VBoxManage command line tool
author: "Max Mustermann (max.muster@example.com)"
'''

EXAMPLES = r'''
- name: "start VM node1"
  tutorial_module_2:
    name: node1
    state: running
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.puzzle.ixtutorial.plugins.module_utils.tutorial_utils import VboxVMS


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                choices=['running', 'poweroff'],
                required=True
            )
        )
    )

    state = module.params['state']
    name = module.params['name']

    vboxvm = VboxVMS(module)

    if name not in vboxvm.get_all():
        module.fail_json(msg='VM %s not installed' % (name))

    if state == "running":
        if name in vboxvm.get_running():
            result = dict(changed=False)
        else:
            vboxvm.start(name)
            result = dict(changed=True)
    elif state == "poweroff":
        if name not in vboxvm.get_running():
            result = dict(changed=False)
        else:
            vboxvm.stop(name)
            result = dict(changed=True)
    else:
        module.fail_json(msg="state %s unsopported" % state)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
