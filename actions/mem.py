import psutil
def get_value():
    """physical memory percent used is %d percent"""
    return psutil.phymem_usage().percent
