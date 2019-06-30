import pexpect
import validators

def is_valid(hostname):
    """
    TODO implement this
    """
    return validators.ipv4(hostname)

def is_up(hostname):
    """
    Check if a host is up.

    @param hostname: ip or host name to check

    @return True: if the host is up
    @return False: if the host is down
    """
    p = pexpect.spawn('ping {hostname} -c 2'.format(hostname=hostname))
    p.wait()
    return p.exitstatus == 0
