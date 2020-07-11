from django.contrib import admin
from .models import Question,Result,Test,Choice,Participent,TestSeries
# Register your models here.

admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Test)
admin.site.register(Choice)
admin.site.register(Participent)
admin.site.register(TestSeries)