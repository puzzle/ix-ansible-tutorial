"""
...
"""


class VboxVMS(object):
    """
    ...
    """

    def __init__(self, module):
        self._module = module

    def __to_list(self, output):
        """
        parse standard output from 'VBoxManage list vms'
        and return a list with VM names
        """

        vmlist = []
        for output_line in output.split('\n'):
            if not output_line:
                continue
            vmlist.append(output_line.split('"')[1])
        return(vmlist)

    def __error(self, rc):
        module.fail_json(
            msg='Running VBoxManage command failed. '
                'Return code: %s. Error: "%s"' % (rc[0], rc[2])
        )

    def get_all(self):
        """
        ...
        """
        rc = self._module.run_command(
            ['VBoxManage', 'list', 'vms']
        )
        if rc[0] != 0:
            self.__error(self._module, rc)
        return(self.__to_list(rc[1]))

    def get_running(self):
        """
        ...
        """
        rc = self._module.run_command(
            ['VBoxManage', 'list', 'runningvms']
        )
        if rc[0] != 0:
            self.__error(self._module, rc)
        return(self.__to_list(rc[1]))

    def start(self, name):
        """
        ...
        """
        rc = self._module.run_command(
            ['VBoxManage', 'startvm', name]
        )
        if rc[0] != 0:
            self.__error(self._module, rc)
        return(self.__to_list(rc[1]))

    def stop(self, name):
        """
        ...
        """
        rc = self._module.run_command(
            ['VBoxManage', 'controlvm', name, 'poweroff']
        )
        if rc[0] != 0:
            self.__error(self._module, rc)
        return(self.__to_list(rc[1]))

