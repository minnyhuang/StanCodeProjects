"""
File: blur.py
Name: Minny
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            new_pixel = new_img.get_pixel(x, y)
            count = 0
            red = 0
            green = 0
            blue = 0
            for a in range(-1, 2, 1):
                for b in range(-1, 2, 1):
                    if (0 < x - a < img.width) and (0 < y - b < img.height):
                        b_pixel = img.get_pixel(x - a, y - b)
                        red += b_pixel.red
                        green += b_pixel.green
                        blue += b_pixel.blue
                        count += 1
                        new_pixel.red = red // count
                        new_pixel.green = green // count
                        new_pixel.blue = blue // count
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
