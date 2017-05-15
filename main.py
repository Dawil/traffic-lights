from time import sleep

RED = 'RED'
YELLOW = 'YELLOW'
GREEN = 'GREEN'

def interval_iter(interval, warn_interval):
    """
    An iterator that accepts the main interval (e.g. 5 minutes) and
    the amount before that interval to warn with yellow lights (e.g.
    30 seconds).
    """
    a_step = interval - warn_interval
    b_step = warn_interval
    count = 0
    while True:
        yield count
        sleep(a_step)
        count += a_step
        yield count
        sleep(b_step)
        count += b_step

def render(label, light):
    return "{}: {}".format(label, light)

def warn_yellow(light):
    if light is GREEN:
        return YELLOW
    else:
        return light

def switch(light):
    if light is YELLOW:
        return RED
    if light is RED:
        return GREEN

if __name__ == '__main__':
    # Initialize the state
    ns = ['NS', RED]
    ew = ['EW', GREEN]

    # Create the timer iterator
    intervals = interval_iter(5,0.5)
    while True:
        # Get the yellow event
        t = next(intervals)
        ns[1] = warn_yellow(ns[1])
        ew[1] = warn_yellow(ew[1])
        print(t, render(*ns), render(*ew))

        # Get the switch event
        t = next(intervals)
        ns[1] = switch(ns[1])
        ew[1] = switch(ew[1])
        print(t, render(*ns), render(*ew))
