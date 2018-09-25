from django.db import models

# Create your models here.,就是写类


class TextUpload(models.Model):
    title = models.CharField(max_length=50,unique=True,verbose_name='标题')
    keywords = models.CharField(max_length=50,unique=True,verbose_name='关键字')
    describe = models.CharField(max_length=100,unique=True,verbose_name='描述')
    content = models.TextField(verbose_name='内容')
    icon = models.ImageField(upload_to='upload', null=True, verbose_name='图片')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        db_table ='text_upload'