from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    gender = models.CharField(max_length=10, choices=[('male', '男'), ('female', '女')], verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    student_id = models.CharField(max_length=20, unique=True, verbose_name='学生ID')
    major = models.CharField(max_length=100, verbose_name='专业')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'
