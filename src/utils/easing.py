
# ported from http://www.gizma.com/easing/
# by http://th0ma5w.github.io
#

import math


# t is the current time (or position) of the tween.
# b is the beginning value of the property.
# c is the change between the beginning and destination value of the property.
# d is the total time of the tween.


class Easing(object):
    @staticmethod
    def linear(t, b, c, d):
        return  c*t/d + b

    @staticmethod
    def easeInQuad(t, b, c, d):
        t /= d
        return c*t*t + b

    @staticmethod
    def easeOutQuad(t, b, c, d):
        t /= d
        return -c * t*(t-2) + b

    @staticmethod
    def easeInOutQuad(t, b, c, d):
        t /= d/2
        if t < 1:
            return c/2*t*t + b
        t-=1
        return -c/2 * (t*(t-2) - 1) + b

    @staticmethod
    def easeInOutCubic(t, b, c, d):
        t /= d/2
        if t < 1:
            return c/2*t*t*t + b
        t -= 2
        return c/2*(t*t*t + 2) + b

    @staticmethod
    def easeInQuart(t, b, c, d):
        t /= d
        return c*t*t*t*t + b

    @staticmethod
    def easeOutQuart(t, b, c, d):
        t /= d
        t -= 1
        return -c * (t*t*t*t - 1) + b

    @staticmethod
    def easeInOutQuart(t, b, c, d):
        t /= d/2
        if t < 1:
            return c/2*t*t*t*t + b
        t -= 2
        return -c/2 * (t*t*t*t - 2) + b

    @staticmethod
    def easeInQuint(t, b, c, d):
        t /= d
        return c*t*t*t*t*t + b

    @staticmethod
    def easeOutQuint(t, b, c, d):
        t /= d
        t -= 1
        return c*(t*t*t*t*t + 1) + b

    @staticmethod
    def easeInOutQuint(t, b, c, d):
        t /= d/2
        if t < 1:
            return c/2*t*t*t*t*t + b
        t -= 2
        return c/2*(t*t*t*t*t + 2) + b

    @staticmethod
    def easeInSine(t, b, c, d):
        return -c * math.cos(t/d * (math.pi/2)) + c + b

    @staticmethod
    def easeOutSine(t, b, c, d):
        return c * math.sin(t/d * (math.pi/2)) + b

    @staticmethod
    def easeInOutSine(t, b, c, d):
        return -c/2 * (math.cos(math.pi*t/d) - 1) + b

    @staticmethod
    def easeInExpo(t, b, c, d):
        return c * pow(2, 10 * (t / d - 1)) + b - c * 0.001

    @staticmethod
    def easeOutExpo(t, b, c, d):
        return  c * 1.001 * (-math.pow(2, -10 * t / d) + 1) + b

    @staticmethod
    def easeInOutExpo(t, b, c, d):
        t /= d/2
        if t < 1:
            return c/2 * math.pow( 2, 10 * (t - 1) ) + b
        t -= 1
        return c/2 * ( -math.pow( 2, -10 * t) + 2 ) + b

    @staticmethod
    def easeInCirc(t, b, c, d):
        t /= d
        return -c * (math.sqrt(1 - t*t) - 1) + b

    @staticmethod
    def easeOutCirc(t, b, c, d):
        t /= d
        t -= 1
        return c * math.sqrt(1 - t*t) + b

    @staticmethod
    def easeInOutCirc(t, b, c, d):
        t /= d/2
        if t < 1:
            return -c/2 * (math.sqrt(1 - t*t) - 1) + b
        t -= 2
        return c/2 * (math.sqrt(1 - t*t) + 1) + b

    @staticmethod
    def easeInExpoConfig(t, b, c, d, base=2, power=10):
        if t == 0:
            return b
        di = c * pow(base, -power)
        return (c+di) * pow(base, power * (t / d - 1)) + b - di


def erange(start, stop, steps, ease=Easing.easeInExpoConfig):
    """
    :type ease: object or str
    """
    import numpy as np
    ease_func = getattr(Easing, ease) if type(ease) is str else ease

    b = start
    c = stop - b
    d = steps
    values = [ease_func(t, b, c, d) for t in range(0, d + 1)]
    values[0] = start
    values[-1] = stop
    return np.array(values)


def ease(time, start=0, stop=100, ease=Easing.easeInExpoConfig):
    """
    :type ease: object or str
    """
    if time <= 0: return start
    if time >= 100: return stop
    ease_f = getattr(Easing, ease) if type(ease) is str else ease
    return ease_f(time, start, stop-start, 100)