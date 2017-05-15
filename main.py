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
    print("{}: {}".format(label, light))

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
    ns = RED
    ew = GREEN

    intervals = interval_iter(5,1)
    while True:
        t = next(intervals)
        print(t)
        ns = warn_yellow(ns)
        ew = warn_yellow(ew)
        render('(N,S)', ns)
        render('(E,W)', ew)
        t = next(intervals)
        print(t)
        ns = switch(ns)
        ew = switch(ew)
        render('(N,S)', ns)
        render('(E,W)', ew)
