from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    contents = models.TextField()

    def __str__(self):
        return self.title
    # 100글자만 출력

    def summary(self):
        return self.contents[:100]
