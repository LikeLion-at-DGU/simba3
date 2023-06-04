from django.db import models

class Category(models.Model):
    category = models.CharField(max_length = 30)

    def __str__(self):
        return self.category

class Keyword(models.Model):
    keyword = models.CharField(max_length = 30)
    def __str__(self):
        return self.keyword
    
class Post(models.Model):
    title = models.TextField()
    writer = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    about_us = models.TextField()
    image = models.ImageField(upload_to='post/', blank=True, null=True)
    categorys = models.ManyToManyField(Category, related_name='categorys', blank=False)
    keywords = models.ManyToManyField(Keyword, related_name='keywords', blank=False)
    def __str__(self):  # title이 대표값
        return self.title
    

