from django.db import models


class UploadImage(models.Model):
    # 上传时间
    date = models.DateField(auto_now=True)
    # 文件大小（kb）
    size = models.IntegerField()
    # 压缩后文件大小（kb）
    compress_size = models.IntegerField(null=True)
    # 原图片分辨率
    resolution = models.CharField(max_length=255)
    # 原图路径
    path = models.CharField(max_length=255)
    # 原图片分辨率
    compress_resolution = models.CharField(max_length=255)
    # 缩略图路径
    compress_path = models.CharField(max_length=255)
    # 图片别名/备注
    alias = models.CharField(max_length=255, null=True)


class Label(models.Model):
    label_name = models.CharField(max_length=255, null=True)
    label_feature = models.CharField(max_length=255, null=True)


class Sort(models.Model):
    """分类"""
    # 分类编号
    sort_feature = models.CharField(max_length=255)
    # 分类名称
    sort_name = models.CharField(max_length=255)
    # 标签
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, to_field="label_feature")



