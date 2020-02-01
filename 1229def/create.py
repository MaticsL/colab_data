
from PIL import Image, ImageFilter
import cv2 as cv
import numpy as np

def ext(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv

def gauss_noise(image):
    h, w, ch = image.shape
    for row in range(h):
        for col in range(w):
        
        	# numpy.random.normal(loc, scale, size)生成高斯分布的概率密度随机数
        	# loc：float代表生成的高斯分布的随机数的均值
        	# scale：float 代表这个分布的方差
        	# size：int or tuple of ints 输出的shape，默认为None，只输出一个值 
        	# 当指定整数时，输出整数个值，也可以输出（a, b）→ a 行 b 列
            s = np.random.normal(0, 10, 3)
            # 去除每一个像素的三个通道值
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            # 在每一个像素的三个通道值上加上高斯噪声
            image[row, col, 0] = ext(b + s[0])
            image[row, col, 1] = ext(g + s[1])
            image[row, col, 2] = ext(r + s[2])
    return image

image_list = [
    '2.jpg'
]
image_list2 = [
    '2.jpg'
]

for i in range(len(image_list)):
    f = image_list[i]
    img = Image.open(f)
    scale = 0.5
    width = int(img.size[0]*scale)
    height = int(img.size[1]*scale)
    img_r = img.resize((width, height), Image.ANTIALIAS)
    img_r.save(f + '.resize.png')
    img_e = img.filter(ImageFilter.EDGE_ENHANCE)
    img_e.save(f + '.edge_enhance.png')
    img = cv.imread('D:\\github\\colab_data\\1229def\\'+ image_list2[i])
    img_n = gauss_noise(img)
    cv.imwrite(f + '.noise.png', img_n)
