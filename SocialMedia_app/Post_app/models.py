from django.db import models
from django.db.models.fields import related
from Auth_app.models import CustomUser

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to='post_image')
    caption = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now = True)
    
    def __str__(self) -> str:
        return self.author.username + ' ' + self.caption
    
    
    class Meta:
        ordering = ['-upload_date',]
        

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='like_post')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='liker')
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.user + ' like ' + self.post
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comment_post')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment_user')
    Comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.Comment

    
