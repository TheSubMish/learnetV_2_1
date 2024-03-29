from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField

from teacher.models import Teacher

import os
from django.db import models

def chapter_file_path(instance, filename):
    # Generate a unique filename based on the chapter title
    if filename is None:
        raise ValidationError('Upload a file')
    base_filename, file_extension = os.path.splitext(filename)
    if file_extension.lower() != '.docx':
        raise ValidationError('Only .docx files are allowed.')
    return f'chapter_files/{instance.chapterName}{file_extension}'

# Create your models here.
cousreCategory = (
    (0,'--------'),
    ('1','HTML'),
    ('2','CSS'),
    ('3','JavaScript'),
    ('4','Python'),
    ('5','Data Analysis'),
    ('6','Data Structure and Algorithms'),
    ('7','Natural Language Processing'),
    ('8','Machine Learning')
)

class Course(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    courseTitle = models.CharField(max_length=100,null=False)
    slug = models.SlugField(max_length=100,null=True)
    courseDescrip = models.TextField(null=False)
    category = models.CharField(max_length=30,choices=cousreCategory)
    courseImage = models.ImageField(upload_to='courseImage',null=False)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.courseTitle)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.courseTitle
    
class Chapter(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    chapterName = models.CharField(max_length=100)
    chapterBody = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chapterName
    
class Test(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    corAns = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question