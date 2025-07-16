from django.db import models
from django.contrib.auth.models import User
from devtools.models import DevTool

class Idea(models.Model):
    title = models.CharField('제목', max_length=200)
    #image = models.ImageField('이미지', blank=True, null=True, upload_to='ideas/%Y/%m/%d')
    content = models.TextField('내용')
    interest = models.IntegerField('관심도', default=0)
    devtool = models.ForeignKey(DevTool, on_delete=models.SET_NULL, null=True, verbose_name='개발툴')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ideas') # 작성자
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class IdeaStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)

    class Meta:
      unique_together = ('user', 'idea')