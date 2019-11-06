from PIL import Image, ImageChops  
import sys

if __name__ == '__main__':
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]

    img1 = Image.open(a)
    img2 = Image.open(b)
    img1_rev = ImageChops.invert(img1)
    result = Image.blend(img1_rev, img2, 0.5)
    result.save(c)
