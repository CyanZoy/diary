# -*- coding: utf-8 -*-
"""
 @Time    : 2018/12/1 17:19
 @Author  : CyanZoy
 @File    : save_image.py
 @Software: PyCharm
 @Describe: 保存图片
 """
import os
import uuid
from app_upload import configuration
from app_upload.models import UploadImage
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def save(data, pic_type):
    """
    保存二进制的图片
    :param data: 图片的二进制数据
    :param pic_type:data的格式[jpg, png ..]
    :return: [code, pic_name]
    """
    code = 1
    data_size = data.size
    uimg = UploadImage()
    uimg.size = data_size/1024  # 数据
    path = BASE_DIR + '/media/images/'
    pic_name = str(uuid.uuid1()) + '.' + pic_type
    uimg.path = pic_name  # 数据
    data_image = data.read()  # 记点: 因为data.read()执行后，data中的数据就空了，所以用变量保存下来
    with open(path + pic_name, 'wb') as file:
        file.write(data_image)  # 保存原图
        uimg.resolution = watermark(path, pic_name)  # 为原图添加水印，后续生成缩略图时无需再添加水印
    if data_size/1024 > configuration.image_max_size:
        uimg.compress_path, uimg.compress_size, uimg.compress_resolution = compress(path, pic_name)

    uimg.save()
    return [code, pic_name]


def compress(path, pic_name):
    """压缩"""
    from PIL import Image
    try:
        image = Image.open(path + pic_name)
    except FileNotFoundError as e:
        print(e)
        return None
    width, height = image.size
    rate = 0.9
    if width >= 2000 or height >= 2000:
        rate = 0.5
    elif width >= 1000 or height >= 1000:
        rate = 0.7
    elif width >= 500 or height >= 500:
        rate = 0.9
    width = int(width * rate)  # 新的宽
    height = int(height * rate)  # 新的高
    image.thumbnail((width, height), Image.ANTIALIAS)  # 生成缩略图
    image.save(path+'compress_'+pic_name)
    return 'compress_'+pic_name, os.path.getsize(path+'compress_'+pic_name)/1024, (width, height)


def watermark(path, pic_name):
    from PIL import ImageDraw, Image, ImageFont
    # 从数据库中读取 水印需要的文字
    image = Image.open(path+pic_name)
    text = 'http://Blog.cyanzoy.top'
    font_size = 20
    width, height = image.size
    if width >= 1000 or height >= 1000:
        font_size += max(int(width/1000)*5, int(height/1000)*5)
    font_size = min(font_size, 35) if font_size > 35 else font_size
    Font = ImageFont.truetype(BASE_DIR+'app_upload/util/simsunb.ttf', font_size)
    # textW, textH = Font.getsize(text)
    d = ImageDraw.Draw(image)
    d.ink = 238 + 240 * 256 + 248 * 256 * 256
    d.text([5, 0], text, font=Font)
    image.save(path+pic_name)
    return width, height
