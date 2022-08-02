from distutils.command.upload import upload
from importlib.resources import contents
from turtle import title
from django.db import models
import os

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/',blank=True)
    field_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/',blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'
    
    def get_absolut_url(self):
        return f'/blog/{self.pk}/'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    