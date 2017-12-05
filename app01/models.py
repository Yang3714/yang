from django.db import models

# Create your models here.

class Userinfo(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)


class Class(models.Model):
    '''
    班级表
    '''
    class_name=models.CharField(max_length=32)
class Student(models.Model):
    '''
    学生表
    '''
    name=models.CharField(max_length=32)
    class_grade=models.ForeignKey(to=Class,verbose_name=("班级"))

class Issue(models.Model):
    '''
    问题表
    '''
    title=models.CharField(max_length=32)

class Questionnaire(models.Model):
    '''
    问卷表
    '''
    name=models.CharField(max_length=32)
    class_grade=models.ForeignKey(to=Class)
    user=models.ForeignKey(to=Userinfo)
class Option(models.Model):
    '''
    选项表
    '''
    issue=models.ForeignKey(to=Issue)
    name=models.CharField(max_length=32)
    score=models.IntegerField(max_length=32)
class Type(models.Model):
    '''
    类型表
    '''
    name=models.CharField(max_length=32)
    issue=models.ForeignKey(to=Issue)
class Answer(models.Model):
    student=models.ForeignKey(to=Student)
    questionnaire=models.ForeignKey(to=Questionnaire)
    option=models.OneToOneField(to=Option)
    content=models.CharField(max_length=255)