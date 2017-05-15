from time import sleep

RED = 'RED'
YELLOW = 'YELLOW'
GREEN = 'GREEN'

def interval_iter(interval, warn_interval):
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
    ns = ('NS', RED)
    ew = ('EW', GREEN)

    intervals = interval_iter(5,1)
    while True:
        t = next(intervals)
        print(t)
        ns[1] = warn_yellow(ns[1])
        ew[1] = warn_yellow(ew[1])
        print(render(*ns))
        print(render(*ew))

        t = next(intervals)
        print(t)
        ns[1] = switch(ns[1])
        ew[1] = switch(ew[1])
        print(render(*ns))
        print(render(*ew))
