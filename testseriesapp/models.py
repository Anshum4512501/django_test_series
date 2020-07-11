from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.



class Participent(models.Model):
    participent = models.OneToOneField(User,on_delete=models.CASCADE)
    participent_name = models.CharField(max_length = 100 )
    participent_joining_date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return str(self.participent)

class TestSeries(models.Model):
    
    participent = models.ManyToManyField(Participent,related_name='paricipent_set',null=True,blank=True)
    test_series_name = models.CharField(max_length=100)
    test_series_description = models.TextField(null=True,blank=True)
    number_of_tests = models.IntegerField()
    price = models.FloatField()
    test_series_joined = models.BooleanField(default=None)
    test_series_joining_date = models.DateTimeField(auto_now=False,null=True ,blank=True)
   
    def __str__(self):
        return self.test_series_name

    def join_test_series(self,request):
        if self.test_series_joined is None:
            print("I m inside model")
            self.test_series_joined = True
            self.participent.add(request.user)
            self.test_series_joining_date = timezone.now()
            print(self.values())    


class Test(models.Model):
    test_series = models.ForeignKey(TestSeries,on_delete=models.CASCADE)
    test_name = models.CharField(max_length = 100)
    test_duration = models.DurationField(default='00:05:00',null=True,blank=True)
    test_max_marks = models.IntegerField(null=True,blank=True)
    number_of_questions = models.IntegerField(null=True ,blank=False)
    def __str__(self):
        return self.test_name  

    

class Question(models.Model):
    test = models.ForeignKey(Test,on_delete=models.CASCADE)
    question_text = models.CharField(max_length = 100)
    question_image = models.ImageField(null=True,blank= True)
    right_choice = models.CharField(max_length= 100,null=True,blank = True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length= 100)
    choosen_choice = models.BooleanField(null=True,blank=True)
    # choosen_option = models.

    def choosen_choice_by_participent(self):
        self.choosen_choice  = True

class Result(models.Model):
    test = models.ForeignKey(Test,on_delete=models.CASCADE)
    number_of_questions_attempted = models.IntegerField(null=True,blank=True)
    gained_marks = models.IntegerField()
    minus_marks = models.IntegerField()
    rank = models.IntegerField()
    taken_time  = models.IntegerField()

    