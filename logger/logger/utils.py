import math
 
TIME_CONVERSION_CONST_ = 10 ** 9

# from https://automaticaddison.com/how-to-convert-a-quaternion-into-euler-angles-in-python/
def euler_from_quaternion(x, y, z, w):
    """
    Convert a quaternion into euler angles (roll, pitch, yaw)
    roll is rotation around x in radians (counterclockwise)
    pitch is rotation around y in radians (counterclockwise)
    yaw is rotation around z in radians (counterclockwise)
    """
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll_x = math.atan2(t0, t1)

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t3, t4)

    return [roll_x, pitch_y, yaw_z] # in radians

def caclulate_rosbot_velocities(x_new, y_new, rpy_new, x_prev, y_prev, rpy_prev, dt):
    """

    """
    # get yaw from [roll, pitch, yaw]
    yaw_new = rpy_new[2]   
    yaw_prev = rpy_prev[2] 
    
    d_yaw = yaw_new - yaw_prev
    d_yaw = (d_yaw + math.pi) % (2 * math.pi) - math.pi
    w = d_yaw / dt

    vx = (x_new - x_prev) / dt
    vy = (y_new - y_prev) / dt
    v = math.sqrt(vx**2 + vy**2)

    alpha = math.atan2(vy,vx)
    v = v * math.cos(alpha - yaw_new)
    return v, w

def convert_ros2_time_to_float(time_tuple):
    """
    
    """
    return float(time_tuple[0] + time_tuple[1]/TIME_CONVERSION_CONST_)
