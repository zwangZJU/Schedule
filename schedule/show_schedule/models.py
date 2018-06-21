# -*- coding: UTF-8 -*- 
from django.db import models

# Create your models here.


class Week(models.Model):
    number = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        # return '{},{},{}'.format(self.number, self.start_date, self.end_date)
        return str(self.number)


class Plan(models.Model):
    member_name = models.CharField(max_length=20)
    work_content = models.CharField(max_length=600)
    is_achievement = models.IntegerField()
    # 关联外键
    week = models.ForeignKey('Week', on_delete=models.CASCADE)

    def __str__(self):
        # return '{},{},{}'.format(self.number, self.start_date, self.end_date)
        return self.member_name
