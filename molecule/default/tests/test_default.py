import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vnc_passwd_file(host):
    f = host.file('/home/vnc/.vnc/passwd')

    assert f.exists
    assert f.user == 'vnc'
    assert f.group == 'vnc'
