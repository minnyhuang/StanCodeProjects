"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# global variables
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.

if_game_start = False


class BreakoutGraphicsPlus:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True

        self.window.add(self.paddle,  x=(self.window.width - self.paddle.width) / 2,
                        y=window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'yellow'

        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

        # Default initial velocity for the ball
        self._dx = 0
        self._dy = 0

        # Initial score
        self.score = 0

        # Bricks number
        self.brick_nums = brick_cols * brick_rows

        # Initialize our mouse listeners
        # 滑鼠點擊後遊戲開始
        onmouseclicked(self.ball_move)
        # 滑鼠拖曳後paddle會跟著移動
        onmousemoved(self.reset_paddle)

        # Draw bricks
        for a in range(brick_cols):
            for b in range(brick_rows):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                if b in (0, 1):
                    self.bricks.fill_color = '#FF88C2'
                    self.bricks.color = '#FF88C2'
                elif b in (2, 3):
                    self.bricks.fill_color = '#FFA488'
                    self.bricks.color = '#FFA488'
                elif b in (4, 5):
                    self.bricks.fill_color = '#FFDD55'
                    self.bricks.color = '#FFDD55'
                elif b in (6, 7):
                    self.bricks.fill_color = '#33FFAA'
                    self.bricks.color = '#33FFAA'
                elif b in (8, 9):
                    self.bricks.fill_color = '#77DDFF'
                    self.bricks.color = '#77DDFF'
                if (a != 1 or b != 6) and (a != 4 or b != 3) and (a != 8 or b != 7):
                    self.window.add(self.bricks, x=(brick_width + brick_spacing) * a,
                                    y=brick_offset + (brick_height + brick_spacing) * b)
        # 繪製特殊的磚塊
        self.bricks_new1 = GRect(brick_width, brick_height)
        self.bricks_new1.filled = True
        self.bricks_new1.fill_color = '#C10066'
        self.window.add(self.bricks_new1, x=45, y=170)

        self.bricks_new2 = GRect(brick_width, brick_height)
        self.bricks_new2.filled = True
        self.bricks_new2.fill_color = '#C10066'
        self.window.add(self.bricks_new2, x=180, y=110)

        self.bricks_new3 = GRect(brick_width, brick_height)
        self.bricks_new3.filled = True
        self.bricks_new3.fill_color = '#C10066'
        self.window.add(self.bricks_new3, x=360, y=190)

        # Label
        # 贏得遊戲時告知玩家獲勝
        self.win_label = GLabel('You Win !!')
        self.win_label.font = '-40'
        self.win_label.color = 'red'
        # 遊戲結束告知玩家輸了
        self.lose_label = GLabel('You Lose :(')
        self.lose_label.font = '-40'
        self.lose_label.color = 'red'
        # 分數板
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = '-20'
        self.score_label.color = 'black'
        self.window.add(self.score_label, x=0, y=self.window.height)

    # 設定paddle可移動範圍為視窗內且y座標固定
    def reset_paddle(self, paddle_x):
        if paddle_x.x - PADDLE_WIDTH/2 > 0 and paddle_x.x + PADDLE_WIDTH/2 < self.window.width:
            self.window.add(self.paddle, x=paddle_x.x-PADDLE_WIDTH/2, y=self.window.height-PADDLE_OFFSET)

    # 當遊戲開始時變換球的速度由靜止變為可動，且移動後判定遊戲開始
    def ball_move(self, click):
        global if_game_start
        if not if_game_start:
            self._dx = random.randint(1, MAX_X_SPEED)
            self._dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self._dx = -self._dx
            if_game_start = True

    # 回歸球數為初始狀態且回到視窗中心並判定遊戲尚未開始
    def ball_restart(self):
        global if_game_start
        self._dx = 0
        self._dy = 0
        if_game_start = False
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

    # 當球碰撞牆壁後需反彈
    def wall_collision(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self._dx = -self._dx
        if self.ball.y <= 0:
            self._dy = -self._dy

    # 回傳球數
    def x_speed(self):
        return self._dx

    def y_speed(self):
        return self._dy

    # 當球碰撞不同物件需有不同動作
    def objects_collision(self):
        # 設定球的四個探針
        obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        obj3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        obj4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        # 當底部的探針碰到paddle則球反彈
        if self.paddle == obj3 or self.paddle == obj4:
            self._dy = -self._dy
        # 當探針碰到物件非paddle時則球反彈且消除物件，並將磚塊總數減一、分數加一，當球反彈時球數增快
        if obj1 is not None and obj1 != self.paddle and obj1 != self.score_label and obj1 != self.bricks_new1\
                and obj1 != self.bricks_new2 and obj1 != self.bricks_new3:
            self.window.remove(obj1)
            self.brick_nums -= 1
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)
            self._dy = self._dy * 1.012
        elif obj2 is not None and obj2 != self.paddle and obj2 != self.score_label and obj2 != self.bricks_new1\
                and obj2 != self.bricks_new2 and obj2 != self.bricks_new3:
            self.window.remove(obj2)
            self.brick_nums -= 1
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)
            self._dy = -self._dy * 1.012
        elif obj3 is not None and obj3 != self.paddle and obj3 != self.score_label and obj3 != self.bricks_new1\
                and obj3 != self.bricks_new2 and obj3 != self.bricks_new3:
            self.window.remove(obj3)
            self.brick_nums -= 1
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)
            self._dy = -self._dy * 1.012
        elif obj4 is not None and obj4 != self.paddle and obj4 != self.score_label and obj4 != self.bricks_new1\
                and obj4 != self.bricks_new2 and obj4 != self.bricks_new3:
            self.window.remove(obj4)
            self.brick_nums -= 1
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)
            self._dy = -self._dy * 1.012
        # 當探針碰到特殊的磚塊則有不同的加分方式
        elif self.bricks_new1 == obj1 or self.bricks_new1 == obj2 or self.bricks_new1 == obj3 or \
                self.bricks_new1 == obj4:
            self.window.remove(self.bricks_new1)
            self.brick_nums -= 1
            self.score += 7
            self.score_label.text = 'Score: ' + str(self.score)
            self._dy = -self._dy * 1.012
        elif self.bricks_new2 == obj1 or self.bricks_new2 == obj2 or self.bricks_new2 == obj3 or \
                self.bricks_new2 == obj4:
            self.window.remove(self.bricks_new2)
            self.brick_nums -= 1
            self.score += 7
            self.score_label.text = 'Score: ' + str(self.score)
            self._dy = -self._dy * 1.012
        elif self.bricks_new3 == obj1 or self.bricks_new3 == obj2 or self.bricks_new3 == obj3 or \
                self.bricks_new3 == obj4:
            self.window.remove(self.bricks_new3)
            self.brick_nums -= 1
            self.score += 7
            self.score_label.text = 'Score: ' + str(self.score)
            self._dy = -self._dy * 1.012
