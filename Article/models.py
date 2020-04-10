from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    user = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%d %m %y %H:%M')
