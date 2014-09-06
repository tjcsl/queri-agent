import os
def get_value():
    """the one minute load average is %.2f"""
    return os.getloadavg()[0]
