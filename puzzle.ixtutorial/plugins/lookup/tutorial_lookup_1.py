# ....

DOCUMENTATION = """
    lookup: tutorial_lookup_1
    short_description: always return fixed string
    description:
      - always return the same fixed string
"""

EXAMPLES = """
- name: Print the string C(Hello, World)
  debug:
    msg: "{{ lookup('tutorial_lookup_1') }} ..."
"""

RETURN = """
_raw:
  description:
    - The string C(Hello, World)
"""

from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        result = "Hello, World"
        return [result]
