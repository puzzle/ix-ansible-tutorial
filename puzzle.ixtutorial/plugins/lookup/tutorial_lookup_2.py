# ....

DOCUMENTATION = """
    lookup: tutorial_lookup_2
    short_description: return random string
    description:
      - return a random string of given length string
      - a prefix string can be specified
    options:
      rand_len:
        description: numer of random chars
        required: False
        default: 8
      rand_chars:
        description: character set to choose from
        required: False
        default: a..z
"""

EXAMPLES = """
- name: Print abc_ following 3 random chars taken from x, y or z
  debug:
    msg: "{{ lookup('puzzle.ixtutorial.tutorial_lookup_2',
                    'abc_',
                    rand_chars='xyz',
                    rand_len=3 ) }}"
- name: Print a random string without prefix of length 10
  debug:
    msg: "{{ lookup('puzzle.ixtutorial.tutorial_lookup_2', rand_len=10 ) }}"
"""

RETURN = """
_raw:
  description:
    - random string
"""

from random import choice
from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        if len(terms) == 0:
            terms = ['']

        rand_chars = kwargs.get('rand_chars', 'abcdefghijklmnopqrstuvwxyz')
        rand_len = int(kwargs.get('rand_len', 8))

        def get_randstring():
            return ''.join(choice(rand_chars) for _ in range(rand_len))

        return [x + get_randstring() for x in terms]
