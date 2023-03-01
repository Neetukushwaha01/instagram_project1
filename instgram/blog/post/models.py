from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    PRIVACY=[
        ('1','private'),
        ('2','public'),
    ]

    image= models.ImageField(upload_to='image',default='p.jpg')
    desc=models.TextField(null=True,blank=True)
    auther=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
    privacy=models.CharField(choices=PRIVACY,default='2',max_length=10)
    like=models.ManyToManyField(User,related_name='like')

    def __str__(self):
        return 'Post '+str(self.id)

