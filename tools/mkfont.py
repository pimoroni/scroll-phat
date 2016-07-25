import os

try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")


font = {}

# font image contains a grid of 3 x 32 characters each of which is
# contained in a 6x6 box. The first character is ASCII 0x20 which
# increments down the column
def load_font():
    font_path = os.path.join(os.path.dirname(__file__), "font.png")
    font_image = Image.open(font_path)

    char = 0x20
    for cx in range(0, 3):
        for cy in range(0, 32):
            char_bits = []

            for x in range(0, 5):
                bits = 0
                for y in range(0, 5):
                    if font_image.getpixel(((cx * 6) + x, (cy * 6) + y)) == 0:
                        bits |= (1 << y)

                char_bits.append(bits)

            # remove all "empty" columns from end of character
            while len(char_bits) > 0 and char_bits[-1] == 0:
                char_bits.pop()

            font[char] = char_bits

            char += 1

load_font()

print("font = " + str(font))
