import psutil
def get_value():
    """there are %d users logged in"""
    return len(psutil.users())
