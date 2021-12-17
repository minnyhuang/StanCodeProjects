"""
File: my_drawing.py
Name: Minny
----------------------
TODO: Drawing a picture by using campy.
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow

window = GWindow(1170, 400, title='My_drawing.py')


def main():
    """
    TODO: 畫了幾何圖形畫得出來的卡通人物
    """
    bg = GRect(1170, 400)
    bg.filled = True
    bg.color = 'orange'
    bg.fill_color = 'orange'
    window.add(bg)

    # 麵包超人
    head_bg = GOval(310, 290, x=395, y=45)
    head_bg.filled = True
    head_bg.color = 'saddlebrown'
    head_bg.fill_color = 'saddlebrown'
    window.add(head_bg)

    head = GOval(300, 280, x=400, y=50)
    head.filled = True
    head.color = 'saddlebrown'
    head.fill_color = 'lightsalmon'
    window.add(head)

    eyebrow_l = GOval(50, 90, x=480, y=90)
    eyebrow_l.color = 'saddlebrown'
    window.add(eyebrow_l)
    eyebrow_l_bg = GRect(50, 60, x=480, y=130)
    eyebrow_l_bg.filled = True
    eyebrow_l_bg.color = 'lightsalmon'
    eyebrow_l_bg.fill_color = 'lightsalmon'
    window.add(eyebrow_l_bg)

    eyebrow_r = GOval(50, 90, x=565, y=90)
    eyebrow_r.color ='saddlebrown'
    window.add(eyebrow_r)
    eyebrow_r_bg = GRect(50, 60, x=565, y=130)
    eyebrow_r_bg.filled = True
    eyebrow_r_bg.color = 'lightsalmon'
    eyebrow_r_bg.fill_color = 'lightsalmon'
    window.add(eyebrow_r_bg)

    mouth = GOval(130, 100, x=485, y=200)
    mouth.filled = True
    mouth.color = 'saddlebrown'
    mouth.fill_color = 'indianred'
    window.add(mouth)
    mouth_bg = GRect(130, 48, x=485, y=200)
    mouth_bg.filled = True
    mouth_bg.color = 'saddlebrown'
    mouth_bg.fill_color = 'lightsalmon'
    window.add(mouth_bg)

    nose = GOval(90, 80, x=505, y=165)
    nose.filled = True
    nose.color = 'saddlebrown'
    nose.fill_color = 'crimson'
    window.add(nose)

    nose_light = GRect(20, 17, x=540, y=175)
    nose_light.filled = True
    nose_light.color = 'white'
    nose_light.fill_color = 'white'
    window.add(nose_light)

    face_l = GOval(90, 90, x=415, y=165)
    face_l.filled = True
    face_l.color = 'saddlebrown'
    face_l.fill_color = 'tomato'
    window.add(face_l)

    face_l_light = GRect(20, 17, x=465, y=190)
    face_l_light.filled = True
    face_l_light.color = 'white'
    face_l_light.fill_color = 'white'
    window.add(face_l_light)

    face_r = GOval(90, 90, x=595, y=165)
    face_r.filled = True
    face_r.color = 'saddlebrown'
    face_r.fill_color = 'tomato'
    window.add(face_r)

    face_r_light = GRect(20, 17, x=615, y=190)
    face_r_light.filled = True
    face_r_light.color = 'white'
    face_r_light.fill_color = 'white'
    window.add(face_r_light)

    eye_l = GOval(30, 45, x=495, y=130)
    eye_l.filled = True
    eye_l.color = 'saddlebrown'
    eye_l.fill_color = 'saddlebrown'
    window.add(eye_l)

    eye_r = GOval(30, 45, x=575, y=130)
    eye_r.filled = True
    eye_r.color = 'saddlebrown'
    eye_r.fill_color = 'saddlebrown'
    window.add(eye_r)

    # 吐司麵包

    head1_bg = GOval(310, 140, x=45, y=26)
    head1_bg.filled = True
    head1_bg.color = 'saddlebrown'
    head1_bg.fill_color = 'saddlebrown'
    window.add(head1_bg)

    head2_bg = GRect(250, 280, x=75, y=65)
    head2_bg.filled = True
    head2_bg.color = 'saddlebrown'
    head2_bg.fill_color = 'saddlebrown'
    window.add(head2_bg)

    head1 = GOval(300, 130, x=50, y=30)
    head1.filled = True
    head1.color = 'White'
    head1.fill_color = 'White'
    window.add(head1)

    head2 = GRect(240, 270, x=80, y=70)
    head2.filled = True
    head2.color = 'White'
    head2.fill_color = 'White'
    window.add(head2)

    mouth1 = GOval(130, 100, x=137, y=210)
    mouth1.filled = True
    mouth1.color = 'saddlebrown'
    mouth1.fill_color = 'indianred'
    window.add(mouth1)
    mouth1_bg = GRect(130, 48, x=137, y=210)
    mouth1_bg.filled = True
    mouth1_bg.color = 'White'
    mouth1_bg.fill_color = 'White'
    window.add(mouth1_bg)

    eyebrow_l2 = GOval(60, 50, x=110, y=100)
    eyebrow_l2.color = 'saddlebrown'
    window.add(eyebrow_l2)
    eyebrow_l2_bg = GRect(60, 60, x=110, y=125)
    eyebrow_l2_bg.filled = True
    eyebrow_l2_bg.color = 'White'
    eyebrow_l2_bg.fill_color = 'White'
    window.add(eyebrow_l2_bg)

    eyebrow_r2 = GOval(60, 50, x=230, y=100)
    eyebrow_r2.color = 'saddlebrown'
    window.add(eyebrow_r2)
    eyebrow_r2_bg = GRect(60, 60, x=230, y=125)
    eyebrow_r2_bg.filled = True
    eyebrow_r2_bg.color = 'White'
    eyebrow_r2_bg.fill_color = 'White'
    window.add(eyebrow_r2_bg)

    eye_l1 = GOval(20, 35, x=130, y=140)
    eye_l1.filled = True
    eye_l1.color = 'saddlebrown'
    eye_l1.fill_color = 'saddlebrown'
    window.add(eye_l1)

    eye_r1 = GOval(20, 35, x=250, y=140)
    eye_r1.filled = True
    eye_r1.color = 'saddlebrown'
    eye_r1.fill_color = 'saddlebrown'
    window.add(eye_r1)

    nose1 = GRect(30, 50, x=185, y=170)
    nose1.filled = True
    nose1.color = 'saddlebrown'
    nose1.fill_color = 'White'
    window.add(nose1)
    nose2 = GRect(30, 20, x=185, y=220)
    nose2.filled = True
    nose2.color = 'saddlebrown'
    nose2.fill_color = 'moccasin'
    window.add(nose2)
    nose1_bg = GRect(30, 20, x=185, y=160)
    nose1_bg.filled = True
    nose1_bg.color = 'White'
    nose1_bg.fill_color = 'White'
    window.add(nose1_bg)

    face_l1 = GOval(30, 30, x=100, y=225)
    face_l1.filled = True
    face_l1.color = 'moccasin'
    face_l1.fill_color = 'moccasin'
    window.add(face_l1)

    face_r1 = GOval(30, 30, x=270, y=225)
    face_r1.filled = True
    face_r1.color = 'moccasin'
    face_r1.fill_color = 'moccasin'
    window.add(face_r1)

    # 咖哩超人

    head3_bg = GOval(310, 270, x=780, y=55)
    head3_bg.filled = True
    head3_bg.color = 'saddlebrown'
    head3_bg.fill_color = 'saddlebrown'
    window.add(head3_bg)

    head3_l_bg = GOval(110, 80, x=755, y=185)
    head3_l_bg.filled = True
    head3_l_bg.color = 'saddlebrown'
    head3_l_bg.fill_color = 'saddlebrown'
    window.add(head3_l_bg)

    head3_r_bg = GOval(110, 80, x=1005, y=185)
    head3_r_bg.filled = True
    head3_r_bg.color = 'saddlebrown'
    head3_r_bg.fill_color = 'saddlebrown'
    window.add(head3_r_bg)

    head3 = GOval(300, 260, x=785, y=60)
    head3.filled = True
    head3.color = 'sienna'
    head3.fill_color = 'sienna'
    window.add(head3)

    head3_l = GOval(100, 70, x=760, y=190)
    head3_l.filled = True
    head3_l.color = 'sienna'
    head3_l.fill_color = 'sienna'
    window.add(head3_l)

    head3_r = GOval(100, 70, x=1010, y=190)
    head3_r.filled = True
    head3_r.color = 'sienna'
    head3_r.fill_color = 'sienna'
    window.add(head3_r)

    eyebrow_l3 = GOval(85, 100, x=850, y=95)
    eyebrow_l3.color = 'black'
    window.add(eyebrow_l3)
    eyebrow_l3_bg = GRect(85, 70, x=850, y=125)
    eyebrow_l3_bg.filled = True
    eyebrow_l3_bg.color = 'sienna'
    eyebrow_l3_bg.fill_color = 'sienna'
    window.add(eyebrow_l3_bg)

    eyebrow_r3 = GOval(85, 100, x=940, y=95)
    eyebrow_r3.color = 'black'
    window.add(eyebrow_r3)
    eyebrow_r3_bg = GRect(85, 70, x=940, y=125)
    eyebrow_r3_bg.filled = True
    eyebrow_r3_bg.color = 'sienna'
    eyebrow_r3_bg.fill_color = 'sienna'
    window.add(eyebrow_r3_bg)

    eye_l3 = GOval(50, 50, x=875, y=130)
    eye_l3.filled = True
    eye_l3.color = 'saddlebrown'
    eye_l3.fill_color = 'White'
    window.add(eye_l3)

    eye_l3_b = GOval(30, 30, x=890, y=140)
    eye_l3_b.filled = True
    eye_l3_b.color = 'saddlebrown'
    eye_l3_b.fill_color = 'saddlebrown'
    window.add(eye_l3_b)

    eye_r3 = GOval(50, 50, x=950, y=130)
    eye_r3.filled = True
    eye_r3.color = 'saddlebrown'
    eye_r3.fill_color = 'White'
    window.add(eye_r3)

    eye_r3_b = GOval(30, 30, x=955, y=140)
    eye_r3_b.filled = True
    eye_r3_b.color = 'saddlebrown'
    eye_r3_b.fill_color = 'saddlebrown'
    window.add(eye_r3_b)

    nose3 = GOval(30, 30, x=922, y=180)
    nose3.filled = True
    nose3.color = 'black'
    nose3.fill_color = 'firebrick'
    window.add(nose3)

    face_l3 = GOval(35, 35, x=800, y=180)
    face_l3.filled = True
    face_l3.color = 'crimson'
    face_l3.fill_color = 'crimson'
    window.add(face_l3)

    face_r3 = GOval(35, 35, x=1035, y=180)
    face_r3.filled = True
    face_r3.color = 'crimson'
    face_r3.fill_color = 'crimson'
    window.add(face_r3)

    mouth3 = GOval(45, 45, x=915, y=230)
    mouth3.filled = True
    mouth3.color = 'maroon'
    mouth3.fill_color = 'maroon'
    window.add(mouth3)

    mouth4l = GOval(40, 40, x=885, y=230)
    mouth4l.filled = True
    mouth4l.color = 'maroon'
    mouth4l.fill_color = 'maroon'
    window.add(mouth4l)

    mouth4r = GOval(40, 40, x=950, y=230)
    mouth4r.filled = True
    mouth4r.color = 'maroon'
    mouth4r.fill_color = 'maroon'
    window.add(mouth4r)

    mouth5l = GOval(35, 35, x=860, y=230)
    mouth5l.filled = True
    mouth5l.color = 'maroon'
    mouth5l.fill_color = 'maroon'
    window.add(mouth5l)

    mouth5r = GOval(35, 35, x=980, y=230)
    mouth5r.filled = True
    mouth5r.color = 'maroon'
    mouth5r.fill_color = 'maroon'
    window.add(mouth5r)

    mouth6l = GOval(30, 30, x=840, y=230)
    mouth6l.filled = True
    mouth6l.color = 'maroon'
    mouth6l.fill_color = 'maroon'
    window.add(mouth6l)

    mouth6r = GOval(30, 30, x=1005, y=230)
    mouth6r.filled = True
    mouth6r.color = 'maroon'
    mouth6r.fill_color = 'maroon'
    window.add(mouth6r)

    mouth7l = GOval(25, 25, x=825, y=230)
    mouth7l.filled = True
    mouth7l.color = 'maroon'
    mouth7l.fill_color = 'maroon'
    window.add(mouth7l)

    mouth7r = GOval(25, 25, x=1025, y=230)
    mouth7r.filled = True
    mouth7r.color = 'maroon'
    mouth7r.fill_color = 'maroon'
    window.add(mouth7r)

    mouth8l = GOval(20, 20, x=810, y=230)
    mouth8l.filled = True
    mouth8l.color = 'maroon'
    mouth8l.fill_color = 'maroon'
    window.add(mouth8l)

    mouth8r = GOval(20, 20, x=1045, y=230)
    mouth8r.filled = True
    mouth8r.color = 'maroon'
    mouth8r.fill_color = 'maroon'
    window.add(mouth8r)

    mouth9l = GOval(15, 15, x=800, y=230)
    mouth9l.filled = True
    mouth9l.color = 'maroon'
    mouth9l.fill_color = 'maroon'
    window.add(mouth9l)

    mouth9r = GOval(15, 15, x=1060, y=230)
    mouth9r.filled = True
    mouth9r.color = 'maroon'
    mouth9r.fill_color = 'maroon'
    window.add(mouth9r)

    mouth10l = GOval(10, 10, x=795, y=230)
    mouth10l.filled = True
    mouth10l.color = 'maroon'
    mouth10l.fill_color = 'maroon'
    window.add(mouth10l)

    mouth10r = GOval(10, 10, x=1070, y=230)
    mouth10r.filled = True
    mouth10r.color = 'maroon'
    mouth10r.fill_color = 'maroon'
    window.add(mouth10r)


if __name__ == '__main__':
    main()
