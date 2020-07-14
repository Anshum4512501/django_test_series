from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView
from .models import Test,TestSeries,Participent,TestSeriesParticipents,Question,Choice,Result
from django.http import JsonResponse 
from django.utils import timezone
import json

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'testseriesapp/home.html'
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(self.request.user)
        participent, created = Participent.objects.get_or_create(participent = self.request.user,participent_name=self.request.user)   
        print(participent,created)
        tsp = participent.testseriesparticipents_set.all()
        print(tsp.values)
        context['testseries'] = TestSeries.objects.all()
        context['tsps']= tsp

        return context

class TestDetailView(DetailView):
    model = TestSeries
    template_name = 'testseriesapp/test_details.html'
    def get_context_data(self,*args,**kwargs):
        context = super(TestDetailView,self).get_context_data(*args,**kwargs)
        context['tests'] = TestSeries.objects.get(pk=self.kwargs.get('pk')).test_set.filter()
        return context 

class QuestionListView(ListView):

    model = Question
    template_name = 'testseriesapp/question_list.html'
    paginate_by = 1


class TestResultDetailView(DetailView):
    model = Test
    template_name = 'testseriesapp/test_result_detail.html'
    context_object_name = 'test'
    # pk_url_kwarg ='pk'
    
    def get_object(self,*args,**kwargs):
        user = self.request.user
        test = get_object_or_404(Test,pk=self.kwargs['pk'])
        test.completed = True
        test.save()
        total_marks = 0
        number_of_questions_attempted = 0
        questions = test.question_set.all()
        for question in questions:
            if question.right_choice == question.choosen_choice:
                total_marks+= question.max_marks
            if question.choosen_choice:
                number_of_questions_attempted+=1
        print(total_marks)
        result,created = Result.objects.get_or_create(test=test)
        print(result,created)
        result.gained_marks = total_marks
        result.number_of_questions_attempted = number_of_questions_attempted
        result.save()
        print(result)        
        print(test)
        print(questions.values())
        return test


def join_test_series_method(request,id):
    
    participent, created = Participent.objects.get_or_create(
    participent = request.user,
    participent_name=request.user.username,
)   
    testseries,created = TestSeries.objects.get_or_create(id=id)
    print("participent,created",participent,created)
    print("Test Series testseries is",testseries)
    tsp,tsp_created = TestSeriesParticipents.objects.get_or_create(participent = participent,testseries =testseries )
    # t.join_test_series(request)
    if tsp.test_series_joined is False or tsp.test_series_joined is None :
            print("I m inside model")
            tsp.test_series_joined = True
            # tsp.participent.add(participent)
            tsp.test_series_joining_date = timezone.now()
            tsp.save()
            print(tsp)
            return JsonResponse("Success fully Joined",safe=False)    
    else:
        return JsonResponse("Allready Joined Joined",safe=False)    
    
def update_choices(request):
    print(request.body)
    json_data = json.loads(request.body)
    choice = get_object_or_404(Choice,pk=json_data['choice_id'])
    question = get_object_or_404(Question,pk=json_data['question_id'])
    choices = question.choice_set.all()
    value = json_data['value']
    for item in choices:
        if item.id == choice.id:
            item.choosen_choice = value
            item.save()
        else:
            item.choosen_choice = None
            item.save()    
    user = request.user
    question.choosen_choice = value
    
    question.save()
    return JsonResponse("update comming from server...%sjsondata.....choice%s....user....%s"%(json_data,choice,user),safe=False)
    