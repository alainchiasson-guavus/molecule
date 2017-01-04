import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('bar')


def test_hostname(SystemInfo):
    assert 'instance-1' == SystemInfo.hostname