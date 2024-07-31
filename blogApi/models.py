from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.TextField(max_length=300)
    photos = models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user.username}-{self.blog[:15]}'
