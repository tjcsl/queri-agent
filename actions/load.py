import os
def get_value():
    """the one minute load average is %d"""
    return os.getloadavg()[0]
