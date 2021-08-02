from django.db import models

from django.db import models
from django.conf import settings

class Problem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None
    )
    problem_order = models.IntegerField(u"題目序數")
    date = models.DateTimeField('日期', null=True)

    RESULT = (('AC', 'AC'),('NA', 'NA'),('WA', 'WA'),('TLE', 'TLE'),('MLE', 'MLE'),('OLE', 'OLE'),('RE', 'RE'),('RF', 'RF'),('CE', 'CE'),('SE', 'SE'))
    result = models.CharField(u'解題狀態',choices=RESULT,max_length=10,default='請選擇科目')

    def __str__(self):
        return self.user.username

    @property
    def showDate(self):
        return str(self.date).split(".")[0].split()[0]
