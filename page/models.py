from django.db import models

GENDER_CHOICE = (
    (u'M', u'Male'),
    (u'F', u'Female'),
)
class Teacher(models.Model):
    tea_id=models.AutoField(max_length=11,primary_key=True)
    tea_nickname=models.CharField(max_length=16,null=False)#教师的登录名
    tea_pas=models.CharField(max_length=16,null=False)
    tea_name=models.CharField(max_length=32,default='AHU0')
    #{{p|displayName:'tea_sex'}}
    tea_sex=models.CharField(max_length=2,choices = GENDER_CHOICE)
    tea_age=models.IntegerField(default=25)
    tea_tel=models.CharField(max_length=11)
    tea_intro=models.TextField(null=True)
    def __str__(self):
        return self.tea_name

class Parent(models.Model):
    par_id=models.AutoField(max_length=11,primary_key=True)
    par_nickname=models.CharField(max_length=16,null=False)
    par_password=models.CharField(max_length=16,null=False)
    par_name=models.CharField(max_length=4,default='Parent0')
    par_sex=models.CharField(max_length=2,choices=GENDER_CHOICE)
    par_tel=models.CharField(max_length=11)

    def __str__(self):
        return self.par_name

class ClassRoom(models.Model):
    cla_id=models.AutoField(max_length=11,primary_key=True)
    cla_name=models.CharField(max_length=4,null=False)
    cla_tea=models.ManyToManyField(Teacher,related_name='cla_tea')
    def __str__(self):
        return self.cla_name

class Student(models.Model):
    stu_id=models.AutoField(max_length=11,primary_key=True)
    stu_name=models.CharField(max_length=32)
    stu_sex=models.CharField(max_length=2,choices=GENDER_CHOICE)
    stu_age=models.IntegerField()
    stu_isAtSch=models.BooleanField(default=False)
    stu_addr=models.TextField(default='NONE')
    stu_perfer=models.TextField(default='NONE')
    stu_parent_id=models.ForeignKey(Parent,related_name='stu_par_set')
    stu_cla=models.ForeignKey(ClassRoom,related_name='syu_cla_set')
    def __str__(self):
        return self.stu_name

class deliverRecord(models.Model):
    deliver_id = models.AutoField(max_length=5,primary_key=True)
    deliver_stu = models.ForeignKey(Student,related_name='stu_deliver_set')
    deliver_par = models.ForeignKey(Parent,related_name='deliver_par_set')
    deliver_choice = models.CharField(max_length=11,default='默认：无')
    deliver_state = models.BooleanField(default=False)
