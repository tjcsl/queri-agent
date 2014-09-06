def get_value():
    """current core temperature is %d degrees celsius"""
    f = open("/sys/class/thermal/thermal_zone0/temp")
    val = int(f.read().strip())
    f.close()
    return val/1000
