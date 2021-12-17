"""
File: bouncing_ball.py
Name: Minny
-------------------------
TODO: This program simulates a bouncing ball at (START_X, START_Y) that
      has VX as x velocity and 0 as y velocity.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

is_in_a_run = True
run = 0

ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
ball.fill_color = 'Black'

window = GWindow(800, 500, title='bouncing_ball.py')
window.add(ball)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(draw)


def draw(click):
    global is_in_a_run, run
    # 分辨是否為同一次點擊內執行與第幾次點擊
    if is_in_a_run and run < 3:
        # 將開關關閉
        is_in_a_run = False
        # 計次為第幾次執行
        run += 1
        count = 0
        while True:
            global GRAVITY, ball
            ball.move(VX, GRAVITY * count)
            if GRAVITY > 0:
                count += 1
            else:
                count -= 1
            # 判斷是否撞擊地面
            if ball.y >= window.height-START_Y:
                GRAVITY = -GRAVITY
                count = count * REDUCE
            # 判斷是否超出邊界
            if ball.x >= window.width:
                window.add(ball, START_X, START_Y)
                GRAVITY = 1
                is_in_a_run = True
                break
            pause(DELAY)


if __name__ == "__main__":
    main()
