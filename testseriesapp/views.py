from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView
from .models import Test,TestSeries,Participent,TestSeriesParticipents,Question,Choice
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
    value = json_data['value']
    user = request.user
    choice.choosen_choice = value
    choice.save()
    return JsonResponse("update comming from server...%sjsondata.....choice%s....user....%s"%(json_data,choice,user),safe=False)
    