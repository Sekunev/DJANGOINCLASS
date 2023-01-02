from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)

    class Meta:
        ordering= ('id',) # Tuple olduğu için ","
        verbose_name = 'Category'

        
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=100, blank=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.title)

    class Meta:
        ordering= ('id',) # Tuple olduğu için ","
        verbose_name = 'Post'




