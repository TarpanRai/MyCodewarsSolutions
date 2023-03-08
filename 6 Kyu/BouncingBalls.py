# A ball is dropped from the nth floor of a building.
# The height of this floor is *h.
# The ball bounces to a certain percentage to it initial height as *bounce.
# The height of a sensor is given as *window.
# How many times will the sensor see the ball pass in front of it, including falling and bouncing


def bouncing_ball(h, bounce, window):
    # To keep track of initial height and after bounce
    current_height = h
    # Count the number of times the ball passes the sensor
    sensor_count = 0
    # Edge case, cause if the ball has a perfect bounce (impossible) the loop never ends
    # and its stupid anyways
    if bounce >= 1 or bounce <= 0:
            return -1
    # Loop until the height of the *bounce is < the height of window
    while current_height > window:
        # Starting height (h) *  bounce percentage
        current_height *= bounce
        # Add 2 to counter for falling and bouncing
        sensor_count += 2
    # -1 cause at the end the ball does not pass the sensor when bouncing but it does when falling
    return sensor_count - 1
