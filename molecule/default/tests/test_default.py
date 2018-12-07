import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_is_haproxy_installed(host):
    package_haproxy = host.package('haproxy')
    assert package_haproxy.is_installed


def test_is_haproxy_running(host):
    haproxy = host.service('demo-haproxy')
    assert haproxy.is_running


def test_is_tcp_mem_configured(host):
    tcpmem = host.sysctl('net.ipv4.tcp_mem')
    assert tcpmem == "47232	78720	94464"


def test_is_non_local_bind_enabled(host):
    nonlocal_bind = host.sysctl('net.ipv4.ip_nonlocal_bind')
    assert nonlocal_bind == 1
