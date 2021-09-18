import cv2 as cv
import numpy as np


def overlapping_filter(lines, sorting_index):
    """
        合并重叠部分
    """
    filtered_lines = []

    lines = sorted(lines, key=lambda lines: lines[sorting_index])

    for i in range(len(lines)):
        l_curr = lines[i]
        if i > 0:
            l_prev = lines[i - 1]
            if (l_curr[sorting_index] - l_prev[sorting_index]) > 5:
                filtered_lines.append(l_curr)
        else:
            filtered_lines.append(l_curr)

    return filtered_lines


def calc_record(filename):
    image = cv.imread(filename)

    # 转灰度
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # 柯西边缘检测
    dst = cv.Canny(gray, 50, 150, None, 3)

    # 霍夫变换
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 350, 6)

    # 检测水平直线
    horizontal_lines = []
    for pt in linesP:
        pt = pt[0]
        if pt[1] == pt[3]:
            horizontal_lines.append(pt)

    horizontal_lines = overlapping_filter(horizontal_lines, 1)
    horizontal_lines = horizontal_lines[3:-1]
    for i, line in enumerate(horizontal_lines):
        cv.line(image, (line[0], line[1]), (line[2], line[3]), (0, 255, 0), 3, cv.LINE_AA)

    # cv.imshow("Source", image)
    # # cv.imshow("Canny", cdstP)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    cv.imwrite("calc_tax_1.png", image)
    return len(horizontal_lines) - 1
    pass


calc_record("./images/koukuan.png")