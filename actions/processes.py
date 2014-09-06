import psutil
def get_value():
    """there are %d processes running right now"""
    return len(psutil.pids())
