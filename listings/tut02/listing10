# ....

DOCUMENTATION = """
    lookup: tutorial_lookup_3
    short_description: fetch device serial number via LDAP
    description:
      - perform LDAP search to find serial number for given CN.
      - pre-requisites: libldap2-dev, libsasl2-dev, python-ldap.
    options:
      ldap_uri:
        description: LDAP URI
        required: True
      search_base:
        description: LDAP search base
        required: True
      search_scope:
        description: LDAP search scope (C(sub), C(one) or C(base))
        required: False
        default: sub
"""

EXAMPLES = """
- name: Fetch serial number for C(node1) via LDAP
  debug:
    msg: "{{ lookup('tutorial_lookup_3', 'device1',
                    ldap_uri='ldap://127.0.0.1',
                    search_base='dc=example,dc=com'  ) }}"
"""

RETURN = """
_raw:
  description:
    - string with serial number
"""

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError, AnsibleLookupError
from ansible.module_utils.basic import missing_required_lib
from ansible.module_utils._text import to_text

PYTHON_LDAP_MISSING = False
try:
    import ldap
    import ldap.filter
except ImportError:
    PYTHON_LDAP_MISSING = True


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        if PYTHON_LDAP_MISSING:
            raise AnsibleLookupError(
                missing_required_lib(
                    'python-ldap',
                    url='https://pypi.org/project/python-ldap/'))

        if len(terms) == 0:
            raise AnsibleError('No devicename given')

        try:
            ldap_uri = kwargs['ldap_uri']
            search_base = kwargs['search_base']
        except KeyError as exc:
            raise AnsibleError('No %s given' % str(exc))

        search_scope = kwargs.get('search_scope', 'sub').lower()

        if search_scope in ('sub', 'subtree'):
            search_scope = ldap.SCOPE_SUBTREE
        elif search_scope == 'one':
            search_scope = ldap.SCOPE_ONELEVEL
        elif search_scope == 'base':
            search_scope = ldap.SCOPE_BASE
        else:
            raise AnsibleError('Unknown LDAP search scope %s' % search_scope)

        ldap_connection = ldap.initialize(ldap_uri)

        def get_serialnumber(devicename):
            ldap_filter = ldap.filter.filter_format(
                u'(&(objectClass=device)(cn=%s))',
                [to_text(devicename)])
            ldap_results = ldap_connection.search_s(
                search_base,
                search_scope,
                ldap_filter,
                attrlist=['serialnumber'])

            return to_text(ldap_results[0][1]['serialNumber'][0])

        return [get_serialnumber(x) for x in terms]
