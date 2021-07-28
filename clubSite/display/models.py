from django.db import models
from django.conf import settings

class Project(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None
    )
    project_name = models.CharField(u"專案名稱",max_length=20)
    description = models.CharField(u"敘述",max_length=600)
    link = models.CharField(u"連結",max_length=200)
    date = models.DateTimeField('發表日期', null=True)

    def __str__(self):
        return self.project_name

    @property
    def showAuthor(self):
        return self.user.username
