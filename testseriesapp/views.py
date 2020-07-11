from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Test,TestSeries,Participent
from django.http import JsonResponse 
from django.utils import timezone

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'testseriesapp/home.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        context['testseries'] = TestSeries.objects.all()
        return context


def join_test_series_method(request,id):
    t = TestSeries.objects.get(id=id)
    participent, created = Participent.objects.get_or_create(
    participent = request.user,
    name=request.user.username,
)
    print("Test Series object is",t)
    print("t.test_series_joined",t.test_series_joined)
    # t.join_test_series(request)
    if t.test_series_joined is False or t.test_series_joined is None :
            print("I m inside model")
            t.test_series_joined = True
            t.participent.add(participent)
            t.test_series_joining_date = timezone.now()
            t.save()
            print(t.values())    
    
    return JsonResponse("Success fully Joined",safe=False)
