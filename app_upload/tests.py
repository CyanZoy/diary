# from django.test import TestCase
from PIL import Image, ImageDraw, ImageFont
image = Image.open('E:/term\diary\media\images/4.png')
# # im.size
# im_resize = im.resize((256, 256)) #default 情况下是NEAREST插值方法
# im_resize0 = im.resize((256,256), Image.BILINEAR)
# # im_resize0.size
# im_resize1 = im.resize((256,256), Image.BICUBIC)
# im_resize2 = im.resize((256,256), Image.ANTIALIAS)
# im_resize2.save('E:/term\diary\media\images/22.png')
width, height = image.size
rate = 1.0 # 压缩率

# 根据图像大小设置压缩率
if width >= 2000 or height >= 2000:
    rate = 0.5
elif width >= 1000 or height >= 1000:
    rate = 0.7
elif width >= 500 or height >= 500:
    rate = 0.9

width = int(width * rate)   # 新的宽
height = int(height * rate) # 新的高

image.thumbnail((width, height), Image.ANTIALIAS) # 生成缩略图

k = 20
text = 'http://Blog.cyanzoy.top'
Font = ImageFont.truetype("C:\Windows\Fonts\simsunb.ttf", k)  # 创建Font对象，k之为字号
textW, textH = Font.getsize(text)            # 获取文字尺寸
d = ImageDraw.Draw(image)
d.ink = 238 + 240 * 256 + 248 * 256 * 256          # 黑色
d.text([int(width/10), 0], text, font=Font)

image.save('E:/term\diary\media\images/watermark.png')



# image.save('E:/term\diary\media\images/44.png')