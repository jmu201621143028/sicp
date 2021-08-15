import turtle


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


def for_each(fun, iterator):
    # 这里用一下，for循环。
    for i in iterator:
        fun(i)


def make_vect(x, y):
    return cons(x, y)
    pass


def xcor_vect(vec):
    return car(vec)


def ycor_vect(vec):
    return cdr(vec)


def add_vect(vec1, vec2):
    return make_vect(xcor_vect(vec1) + xcor_vect(vec2),
                     ycor_vect(vec1) + ycor_vect(vec2))
    pass


def sub_vect(vec1, vec2):
    return make_vect(xcor_vect(vec1) - xcor_vect(vec2),
                     ycor_vect(vec1) - ycor_vect(vec2))
    pass


def scale_vect(s, vec):
    return make_vect(s * xcor_vect(vec), s * ycor_vect(vec))


def make_segment(point_begin, point_end):
    return cons(point_begin, point_end)


def start_segment(seg):
    return car(seg)


def end_segment(seg):
    return cdr(seg)


def make_frame(origin, edge1, edge2):
    return cons(origin, cons(edge1, edge2))
    pass


def origin_frame(frame):
    return car(frame)
    pass


def edge1_frame(frame):
    return car(cdr(frame))
    pass


def edge2_frame(frame):
    return cdr(cdr(frame))
    pass


def frame_coord_map(frame):
    return lambda v: add_vect(origin_frame(frame),
                              add_vect(scale_vect(xcor_vect(v), edge1_frame(frame)),
                                        scale_vect(ycor_vect(v), edge2_frame(frame))))


def transform_painter(painter, origin, corner1, corner2):
    m = frame_coord_map(frame)
    new_origin = m(origin)
    return lambda frame: painter(
        make_frame(
            new_origin,
            sub_vect(m(corner1), new_origin),
            sub_vect(m(corner2), new_origin)
        )
    )


def filp_vert(painter):
    return transform_painter(
        painter,
        make_vect(0.0, 1.0),            # origin
        make_vect(1.0, 1.0),            # edge1
        make_vect(0.0, 0.0)             # edge2
    )


def draw_line(start, end):
    turtle.up()    # 画笔拿起
    turtle.setpos(xcor_vect(start), ycor_vect(start))
    turtle.down()  # 画笔落下
    turtle.setpos(xcor_vect(end), ycor_vect(end))
    pass


def segments2painter(segment_list):
    return lambda frame: for_each(lambda segment:
                                  draw_line(
                                            (frame_coord_map(frame)(start_segment(segment))),
                                            (frame_coord_map(frame)(end_segment(segment)))
                                            ),
                                  segment_list)

seg_list = []
seg_list.append(make_segment(make_vect(3, 6), make_vect(2, 5)))
seg_list.append(make_segment(make_vect(2, 5), make_vect(3, 4)))
seg_list.append(make_segment(make_vect(3, 4), make_vect(2, 4)))
seg_list.append(make_segment(make_vect(2, 4), make_vect(1, 3)))
seg_list.append(make_segment(make_vect(1, 3), make_vect(0, 4)))
seg_list.append(make_segment(make_vect(0, 3), make_vect(1, 2)))
seg_list.append(make_segment(make_vect(1, 2), make_vect(2, 3)))
seg_list.append(make_segment(make_vect(2, 3), make_vect(3, 2)))
seg_list.append(make_segment(make_vect(3, 2), make_vect(2, 0)))
seg_list.append(make_segment(make_vect(5, 3), make_vect(6, 0)))
seg_list.append(make_segment(make_vect(5, 3), make_vect(7, 2)))
seg_list.append(make_segment(make_vect(6, 4), make_vect(7, 3)))
seg_list.append(make_segment(make_vect(4, 4), make_vect(6, 4)))
seg_list.append(make_segment(make_vect(5, 5), make_vect(4, 4)))
seg_list.append(make_segment(make_vect(4, 6), make_vect(5, 5)))


frame = make_frame(make_vect(100, 100), make_vect(10, 0), make_vect(0, 10))
segments2painter(seg_list)(frame)

segments2painter(seg_list)

for i in range(-200, 200, 28):
    frame = make_frame(make_vect(-i, 0), make_vect(5, 0), make_vect(5, 15))
    segments2painter(seg_list)(frame)
turtle.done()
pass