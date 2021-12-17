"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        # 球超出視窗下面邊界扣一條命
        if graphics.ball.y > graphics.window.height:
            lives -= 1
            # 若剩餘的命不為0則遊戲繼續且回歸初始狀態
            if lives > 0:
                graphics.ball_restart()
            # 若無剩餘的命數則遊戲結束且告知玩家輸了
            else:
                graphics.window.add(graphics.lose_label, x=(graphics.window.width - graphics.win_label.width) / 2,
                                    y=100)
                break
        # 若無磚塊則遊戲結束且告知玩家贏了
        if graphics.brick_nums == 0:
            graphics.window.add(graphics.win_label, x=(graphics.window.width - graphics.win_label.width) / 2,
                                y=100)
            break
        # 回傳移動的球數
        graphics.ball.move(graphics.x_speed(), graphics.y_speed())
        # 球碰撞牆壁後反彈
        graphics.wall_collision()
        # 球碰撞物件後反彈且有不同動作
        graphics.objects_collision()
        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
