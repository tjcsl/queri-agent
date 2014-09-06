def get_value():
    """there are %d bits of entropy available"""
    f = open("/proc/sys/kernel/random/entropy_avail")
    val = int(f.read().strip())
    f.close()
    return val
