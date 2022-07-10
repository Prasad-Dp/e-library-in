from distutils.command import upload
from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name=models.CharField(max_length= 45)
    book_slug=AutoSlugField(populate_from='book_name',unique=True,null=True,default=None)
    book_des=models.TextField()
    book_img=models.ImageField(upload_to='thumbnails')
    book_file=models.FileField(upload_to='book_files')
    book_author=models.CharField(max_length=50)
    book_publisher=models.CharField(max_length=50)
    book_gener=models.CharField(max_length=20)
    book_year=models.CharField(max_length=5)
    book_cost=models.CharField(max_length= 50)

    def __str__(self):
        return self.book_name
        
