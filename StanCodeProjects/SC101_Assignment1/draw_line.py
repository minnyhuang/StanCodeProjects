"""
File: draw_line.py
Name: Minny
-------------------------
TODO: Drawing a line on an instance of GWindow class.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 10

# Global variable
window = GWindow()
count = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(click):
    global count, x1, y1, x2, y2
    point = GOval(SIZE, SIZE, x=click.x - SIZE / 2, y=click.y - SIZE / 2)
    point.filled = False
    window.add(point)
    count += 1
    # 抓取起點的座標
    first_point = window.get_object_at(x1, y1)
    # 分辨為起點還是終點
    if count % 2 == 1:
        x1 = click.x
        y1 = click.y
    elif count % 2 == 0:
        x2 = click.x
        y2 = click.y
        line = GLine(x1, y1, x2, y2)
        line.filled = True
        line.fill_color = 'Black'
        window.add(line)
        # 移除圓點
        window.remove(first_point)
        window.remove(point)


if __name__ == "__main__":
    main()
