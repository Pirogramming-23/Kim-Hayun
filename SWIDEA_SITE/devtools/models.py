from django.db import models

# Create your models here.
class DevTool(models.Model):
    name = models.CharField('개발툴 이름', max_length=100)
    kind = models.CharField('종류', max_length=100)
    content = models.TextField('설명')
    
    def __str__(self):
        return self.name