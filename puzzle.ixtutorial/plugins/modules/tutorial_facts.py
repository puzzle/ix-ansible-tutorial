#!/usr/bin/python
# ...

DOCUMENTATION = r'''
---
module: tutorial_facts
short_description: Get current users
description:
     - Query users that are currently logged in
author:
  - ...
'''

EXAMPLES = r'''
- name: Populate C(current_users) facts
  tutorial_facts:

- debug:
    var: ansible_facts.current_users
'''

RETURN = r'''
ansible_facts:
  description: dict with users
  returned: always
  type: complex
  contains:
    current_users:
'''


from ansible.module_utils.basic import AnsibleModule
import psutil


def main():
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    module.run_command_environ_update = dict(LANG="C", LC_ALL="C")
    current_users = [x._asdict() for x in psutil.users()]
    results = dict(ansible_facts=dict(current_users=current_users))
    module.exit_json(**results)

    
if __name__ == '__main__':
    main()
