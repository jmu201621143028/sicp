import math

###############################################################
def cons(x, y):
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y
        else:
            raise Exception('Argument not 0 or 1')
    return dispatch


def car(z):
    return z(0)


def cdr(z):
    return z(1)

#############################################################
def attach_tag(type_tag, contents):
    return cons(type_tag, contents)


def type_tag(datum):
    return car(datum)


def contens(datum):
    return cdr(datum)


def rectangular(z):
    if type_tag(z) == "rectangular":
        return True
    return False

def polar(z):
    if type_tag(z) == "polar":
        return True
    return False

#############################################################
# 直角坐标
def real_part_rectangular(z):
    return car(z)

def imag_part_rectangular(z):
    return cdr(z)

def mangnitude_rectangular(z):
    return math.sqrt(real_part_rectangular(z)**2 + imag_part_rectangular(z)**2)

def angle_rectangular(z):
    return math.atan(imag_part_rectangular(z) / real_part_rectangular(z))

def make_from_real_imag_rectangular(x, y):
    return attach_tag("rectangular", cons(x, y))

def make_from_mag_ang_rectangular(r, a):
    return attach_tag("rectangular", cons(r * math.cos(a), r * math.sin(a)))

#############################################################
# 极坐标
def magnitude_polar(z):
    return car(z)

def angle_polar(z):
    return cdr(z)

def real_part_polar(z):
    return magnitude_polar(z) * math.cos(angle_polar(z))

def imag_part_polar(z):
    return magnitude_polar(z) * math.sin(angle_polar(z))

def make_from_real_imag_polar(x, y):
    return attach_tag('polar', cons(math.sqrt(x**2, y**2), math.atan(y / x)))

def make_from_mag_ang_polar(r, a):
    return attach_tag('polar', cons(r, a))

#################################################
def real_part(z):
    if rectangular(z):
        return real_part_rectangular(z)
    elif polar(z):
        return real_part_polar(z)
    else:
        raise Exception('Unknown type')


def imag_part(z):
    if rectangular(z):
        return imag_part_rectangular(z)
    elif polar(z):
        return imag_part_polar(z)
    else:
        raise Exception('Unknown type')

def magnitude(z):
    if rectangular(z):
        return mangnitude_rectangular(z)
    elif polar(z):
        return magnitude_polar(z)
    else:
        raise Exception('Unknown type')

def angle(z):
    if rectangular(z):
        return angle_rectangular(z)
    elif polar(z):
        return angle_polar(z)
    else:
        raise Exception('Unknown type')
#################################################
def make_from_real_imag(x, y):
    return make_from_real_imag_rectangular(x, y)

def make_from_mag_ang(r, a):
    return make_from_mag_ang_polar(r, a)

#################################################
def add_complex(z1, z2):
    return make_from_real_imag(
        real_part(z1) + real_part(z2),
        imag_part(z1) + imag_part(z2)
    )

def sub_complex(z1, z2):
    return make_from_real_imag(
        real_part(z1) - real_part(z2),
        imag_part(z1) - imag_part(z2)
    )

def mul_complex(z1, z2):
    return make_from_mag_ang(
        magnitude(z1) * magnitude(z2),
        angle(z1) + angle(z2)
    )

def div_complex(z1, z2):
    return make_from_mag_ang(
        magnitude(z1) / magnitude(z2),
        angle(z1) - angle(z2)
    )

